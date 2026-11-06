
import smtplib
from email.message import EmailMessage

sender_email = "your_email@gmail.com"
sender_password = "your_16_digit_app_password"
receiver_email = "receiver@gmail.com"

msg = EmailMessage()
msg["Subject"] = "Job Application - Python Developer"
msg["From"] = sender_email
msg["To"] = receiver_email

msg.set_content("""
Hello,

I am interested in the Python Developer position.
Please find my resume attached.

Thank you.

Regards,
Praveen
""")

try:
    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
        server.login(sender_email, sender_password)
        server.send_message(msg)

    print("Email sent successfully!")

except Exception as e:
    print("Error:", e)


# - Hr@alarayan.com
# 2- Wadaef2019@abdulla-fouad.com
# 3- Hr.qrm@hotmail.com
# 4- Rec@alojaimi.com
# 5- Recruitment@rawabiholding.com
# 6- Job.s6@hotmail.com
# 7- Careers@dnata.com
# 8- Hr@alesayi_motors.com
# 9- CV@Arabianfal.com
# 10- Recruiting.ksa@mcmermott.com
# 11- Recruitment@aytb.com
# 12- Wadaef@gtecorp.com
# 13- Careers@nesr.com
# 14- Recruit@farm.com.sa
# 15- Info@alhumamlaw.com
# 16- Hr1@gulfteksaudi.com
# 17- Catcosa@catcosa.com
# 18- Cv@tafear.com
# 19- Recruitment@sraco.com.sa
# 20- Info@atco.com.sa
# 21- HRdepartmental@sa.yokogawa.com
# 22- Recruitment@shadeco.com
# 23- Klc.hr@alkafaa.com
# 24- Kbr-amcdehr@kbr.com
# 25- Recruitment@batook.com
# 26- Career@shawarmer.com
# 27- Hrsupport@archirodon.net
# 28- Jobs@binajinah.com
# 29- Marketing.np@nesma.com
# 30- Cv@aldawaa.com.sa
# 31- Careers@innosoft.sa
# 32- M@startime.com.sa
# 33- job@musk.sa.com
# 34- Shababwatansa@gmail.com
# 35- j@sabksa.com
# 36- al.alshaikh@bonyan.sa
# 37- ymohammed@innovest.com.sa
# 38- al.alshaikh@bonyan.sa
# 39- s.alwadi@nhc.sa
# 40- i.atassi@artar.com.sa
# 41- oalkhunaizi@darwaemaar.com
# 42- jobs@almasah.net
# 43- recruitment.amjad@gmail.com
# 44- jobrydlaw@gmail.com
# 45- Job@almoosahospital.com.sa
# 46- recruitment@almoosahospital.com.sa
# 47- jobs@sghgroup.net
# 48- career.dmm@sghgroup.net
# 49- talent.acquisition@drsulaimanalhabib.com
# 50- Careers@jhah.com
# 51- hrd@alahsahospital.com.sa
# 52- career@almanahospital.com.sa
# 53- info@familycare.com.sa
# 54- info@ramclinics.com
# 55- HR.DSFHR@fakeeh.care
# 56- career@mouwasat.com
# 57- careers@dallah-hospital.com
# 58- hr.phc@drsulaimanalhabib.com
# 59- careers@almurjanhospital.com
# 60- hiringnow.ksa@gmail.com
# 61- talent.acquisition@drsulaimanalhabib.com