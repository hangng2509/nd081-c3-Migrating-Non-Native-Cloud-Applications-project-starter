import logging
import azure.functions as func
import psycopg2
import os
from datetime import datetime
from sendgrid import SendGridAPIClient, Email, To, Content
from sendgrid.helpers.mail import Mail, HtmlContent


def main(msg: func.ServiceBusMessage):

    notification_id = int(msg.get_body().decode('utf-8'))
    logging.info('Python ServiceBus queue trigger processed message: %s',notification_id)
    #Connect to db 
    conn = psycopg2.connect(user="admin123@techconfdb-server-lab-3",
                                    password="admin@Ne123",
                                    host="techconfdb-server-lab-3.postgres.database.azure.com",
                                    port="5432",
                                    database="techconfdb")
    cursor = conn.cursor()

    try:
        # Get notification message and subject from database using the notification_id
        notification_query = '''SELECT subject, message 
                                FROM notification
                                WHERE id = {};'''
        cursor.execute(notification_query.format(notification_id))

        # Get attendee email and name by notification id
        notification = cursor.fetchone()
        subject = notification[0]
        message = notification[1]

        # Loop through each attendee and send an email with a personalized subject
        cursor.execute("SELECT email, first_name FROM attendee;")
        attendees = cursor.fetchall()
    
        status = "Notified {} attendees".format(len(attendees))
        cursor.execute("UPDATE notification SET status = '{}', completed_date = '{}' WHERE id = {};".format(status, datetime.utcnow(), notification_id))
        conn.commit()

    except (Exception, psycopg2.DatabaseError) as error:
        logging.error(error)
        conn.rollback()
    finally:
        if conn:
            cursor.close()
            conn.close()
            

def send_email(email, subject, body):
    message = Mail(
        from_email=os.environ.get('ADMIN_EMAIL_ADDRESS'),
        to_emails=email,
        subject=subject,
        plain_text_content=body)
    try:
        sg = SendGridAPIClient(os.environ.get('SENDGRID_API_KEY'))
        sg.send(message)
    except Exception as e:
        logging.error(e)