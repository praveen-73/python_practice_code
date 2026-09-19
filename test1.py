# import tkinter as tk
# from tkinter import messagebox

# root = tk.Tk()
# root.withdraw()  # Hide the main window

# messagebox.showinfo("Success", "Process completed successfully!")



​if 0 == 0: #range
    def switch_to_window_by_title(driver, title_keyword, timeout=15):
        end_time = time.time() + timeout
        while time.time() < end_time:
            for handle in driver.window_handles:
                driver.switch_to.window(handle)
                if title_keyword.lower() in driver.title.lower():
                    print(f"Switched | Title: {driver.title}")
                    return True
            time.sleep(0.5)
        return False
    import traceback
    is_Exception = False
    from droid_activities import date_time
    currentdate = date_time.date_time('%m-%d-%Y', 'current',0, "currentdate","currentdate")
    print(currentdate)
    from droid_activities import messagebox 
    #messagebox.popup_message_box(currentdate.replace('-','/'))
    outerretry = int(1) #int
    sucessboolean = bool(True) #bool@droidal.com
    from droid_activities import FileExists
    summaryfileexist = FileExists.file_exists('C:\\RisePT\\Daily Summary Folder'+'\\'+'RisePT_PatientCoordination_SummaryReport - '+currentdate.replace('-','.')+'.xlsx')
    if summaryfileexist != True: #range
        from droid_activities import copyfile
        copyfile.copy_file(r'c:\RisePT\Summary Template\SummaryTemplatexlsx_PatientCoordination.xlsx','C:\\RisePT\\Daily Summary Folder'+'\\'+'RisePT_PatientCoordination_SummaryReport - '+currentdate.replace('-','.')+'.xlsx')
#End If summaryfileexist = False
    from droid_activities import date_time
    yesterday_Date = date_time.date_time('%m-%d-%Y', 'before',1, "currentdate", "currentdate")
    print(yesterday_Date)
    Temp_File =(r'C:\RisePT\Input File\TextTask2_InputFile'+'RisePT_2texttask_inputReport - '+currentdate.replace('-','.')+'.xlsx')
    print(Temp_File)
    from droid_activities import FileExists
    # Text2fileexist = FileExists.file_exists('C:\RisePT\Input File\TextTask2_InputFile'+'RisePT_2texttask_inputReport - '+currentdate.replace('-','.')+'.xlsx')
    Text2fileexist = FileExists.file_exists(r'C:\RisePT\Input File\TextTask2_InputFile\\' +'RisePT_2texttask_inputReport - ' +currentdate.replace('-','.') +'.xlsx')
    if Text2fileexist != True: #range
        from droid_activities import copyfile
        copyfile.copy_file(r'c:\RisePT\Summary Template\TextTask2_PatientsReport_Template.xlsx','C:\\RisePT\\Input File'+'\\'+'TextTask2_InputFile'+'\\'+'RisePT_2texttask_inputReport - '+currentdate.replace('-','.')+'.xlsx')
    while outerretry<=1: #Outer Retry
        try: #Try Start - Outer Retry Logic
            #Ivoke started EMR Login
            from droid_activities import assetfetch
            url = assetfetch.asset_get(1101)
            from droid_activities import assetfetch
            username = assetfetch.asset_get(1102)
            from droid_activities import assetfetch
            password = assetfetch.asset_get(1103)
            import time
            time.sleep(2)
            from droid_activities import openbrowser
            driver = openbrowser.open_browser(
                "Chrome()",
                "https://go.promptemr.com/",
                3,
                "full-width",
                r"C:\Program Files\Google\Chrome\Application\chrome.exe"  # ← add this
            )
            time.sleep(3)
            # import subprocess
            # import time
            # chrome_path = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
            # user_data_dir = r"C:\Users\DRD-DEV-0050\AppData\Local\Google\Chrome\User Data\Profile 1"
            # remote_debugging_port = "9222"
            # command = f'"{chrome_path}" --remote-debugging-port={remote_debugging_port} --user-data-dir="{user_data_dir}"'
            # subprocess.Popen(command, shell=True)
            time.sleep(3)
            # from droid_activities import messagebox
            # messagebox.popup_message_box('Starting the Performer Process')
            launchcount = int(0) #int
            try: #Try Start - Launch an Login EMR Portal
                #Ivoke started Image EMR Login
                import time
                time.sleep(6)
                # from droid_activities import citriximageclick_simulate
                # citriximageclick_simulate.citrix_image_click(r"C:\RisePT\Image Folder\Prompt EMR.png", 0.8)
                # import time
                # time.sleep(5)
                from droid_activities import CitrixImageExist
                username_Exists = CitrixImageExist.citrix_image_exist(r"C:\RisePT\Image Folder\username.png",10, 0.8)
                if(username_Exists):
                    from droid_activities import citirix_image_typeinto
                    citirix_image_typeinto.image_typeinto(r"C:\RisePT\Image Folder\username.png", 0.8,'risept@droidal.com')
                    import time
                    time.sleep(2)
                    from droid_activities import citirix_image_typeinto
                    citirix_image_typeinto.image_typeinto(r"C:\RisePT\Image Folder\password.png", 0.8,'Droidal@2025')
                    import time
                    time.sleep(2)
                    try:
                        from droid_activities import citriximageclick_simulate
                        citriximageclick_simulate.citrix_image_click(r"C:\RisePT\Image Folder\verifyhuman.png", 0.8)
                    except:
                        print('No Verify human box')
                    import time
                    time.sleep(10)
                    from droid_activities import citriximageclick_simulate
                    citriximageclick_simulate.citrix_image_click(r"C:\RisePT\Image Folder\loginbutton.png", 0.8)
                    from droid_activities import message_box_delay
                    message_box_delay.show_timed_message_box('First Image Process of Clicking Login Success', 1)
                import time
                time.sleep(1)
                # from droid_activities import openbrowser_debugger_v1
                # driver=openbrowser_debugger_v1.df_browser_with("Chrome()", 'https://go.promptemr.com/onDeck?tab=upcoming',15,"full-width")
                # import time
                # time.sleep(2)
            except:
                print("Emr Portal issue")
                import traceback
                Er = traceback.format_exc()
                print(f"An error occurred: {Er}")
            # WEAVE PORTAL < ------------------- Login Weave Portal ------------------->
            import keyboard
            keyboard.press_and_release('ctrl+t')
            from droid_activities import openbrowser
            from droid_activities import windowhandle
            windowhandle.window_handle(driver,1)
            time.sleep(5)
            import pyautogui;import time;pyautogui.hotkey('ctrl', 'l');time.sleep(1);pyautogui.write('https://auth.getweave.com/?login=&username=');pyautogui.press('enter');
            import time
            time.sleep(5)
            windowhandle.window_handle(driver,1)
            print("Handle:", driver.current_window_handle)
            print("URL:", driver.current_url)
            print("Title:", driver.title)
            while(True):
                from droid_activities import ElementWait
                login_pageexist = ElementWait.element_wait(driver, "By.XPATH", f"//img[@alt='weave-app-logo']",10)
                launchcount = int(0) #int
                if login_pageexist == True: #range
                    from droid_activities import message_box_delay
                    message_box_delay.show_timed_message_box('Launch Page Exist - Weave Process', 1)
                    #End If - Launch Page Exist
                else: #Else Start - No Launch Page Exist
                    import time
                    time.sleep(5)
                    from droid_activities import message_box_delay
                    message_box_delay.show_timed_message_box('No Launch Page Exist - Weave Process', 1)
                import time
                time.sleep(3)
                from droid_activities import ClickElement
                ClickElement.click_element("By.XPATH", "xpath",f"//label[normalize-space(text())='Email']/following-sibling::input[1]",1,"Login Button",driver)
                from droid_activities import TypeElement
                TypeElement.type_element("By.XPATH", "xpath",f"//label[normalize-space(text())='Email']/following-sibling::input[1]",'risept@droidal.com',1,driver,"UserName")
                time.sleep(1)
                from droid_activities import ClickElement
                ClickElement.click_element("By.XPATH", "xpath",f"//label[normalize-space()='Password']/following-sibling::input[1]",1,"Login Button",driver)
                from droid_activities import TypeElement
                TypeElement.type_element("By.XPATH", "xpath",f"//label[normalize-space()='Password']/following-sibling::input[1]",'weavepassword@2026',1,driver,"Password")
                time.sleep(1)
                from droid_activities import ClickElement
                ClickElement.click_element("By.XPATH", "xpath",f"//button[.//span[normalize-space()='Log In']]",1,"Login Button",driver)
                import time
                time.sleep(15)
                from droid_activities import ElementWait
                Contact_exist = ElementWait.element_wait(driver, "By.XPATH", f"//a[.//span[normalize-space()='Contacts']]",10)
                if(Contact_exist):
                    print("Login SucessFull")
                    break
                else:
                    print("Login Un Successfull")
                    import time
                    time.sleep(5)
             #<------------------------ Login Solumn Portal --------------------------->     
            import keyboard
            keyboard.press_and_release('ctrl+t')
            from droid_activities import windowhandle
            windowhandle.window_handle(driver,2)
            time.sleep(4)
            import pyautogui;import time;pyautogui.hotkey('ctrl', 'l');time.sleep(1);pyautogui.write('https://app.getsolum.com/login');pyautogui.press('enter');
            import time
            time.sleep(5)
            from droid_activities import ElementWait
            login_pageexist = ElementWait.element_wait(driver, "By.XPATH", f"//img[@alt='Logo' and contains(@src, 'logo')]",10)
            launchcount = int(0) #int
            if login_pageexist == True: #range
                from droid_activities import message_box_delay
                message_box_delay.show_timed_message_box('Launch Page Exist - Solumn Process', 1)
                #End If - Launch Page Exist
            else: #Else Start - No Launch Page Exist
                import time
                time.sleep(5)
                from droid_activities import message_box_delay
                message_box_delay.show_timed_message_box('No Launch Page Exist - Solumn Process', 1)
                #Else End - No Launch Page Exist
            import time
            time.sleep(3)
            from droid_activities import TypeElement
            TypeElement.type_element("By.XPATH", "xpath",f"//input[@name='email']",'risept@droidal.com',1,driver,"Email")
            time.sleep(1)
            from droid_activities import TypeElement
            TypeElement.type_element("By.XPATH", "xpath",f"//input[@id='password']",'Risept@@2027',1,driver,"Password")
            time.sleep(1)
            from droid_activities import ClickElement
            ClickElement.click_element("By.XPATH", "xpath",f"//button[@type='submit']",1,"Login Button",driver)
            import time
            time.sleep(5)
            # <---------------- Login Solum Completed ------------------------>
            from droid_activities import windowhandle
            switch_to_window_by_title(driver, "prompt")
            time.sleep(5)
            from droid_activities import CitrixImageExist
            RestorePage_Exists = CitrixImageExist.citrix_image_exist(r"C:\RisePT\Image Folder\Restore_Page.png",10, 0.7)
            if(RestorePage_Exists):
                from droid_activities import citriximageclick_simulate
                citriximageclick_simulate.citrix_image_click(r"C:\RisePT\Image Folder\Restore_Button.png", 0.8)
                time.sleep(5)
            from droid_activities import ElementWait
            homepage_exist = ElementWait.element_wait(driver, "By.XPATH", f"(//div[contains(text(), 'On Deck')])[1]",20)
            if homepage_exist == True: #range #< -------------------------- EMR PORTAL------------------> #Need to command
                from droid_activities import windowhandle
                switch_to_window_by_title(driver, "prompt")
                from droid_activities import message_box_delay
                message_box_delay.show_timed_message_box('Home Page Exist - Login Successful - PROMPT EMR Portal', 1)
                import time
                time.sleep(2)
                from droid_activities import ClickElement
                ClickElement.click_element("By.XPATH", "xpath",f"//div[normalize-space(text())='Reports']",1,"Reports Menu",driver)
                import time
                time.sleep(1)
                from droid_activities import ClickElement
                ClickElement.click_element("By.XPATH", "xpath",f"//div[contains(@class, 'q-tab__label') and normalize-space(text())='Operations']",1," Operation Menu",driver)
                time.sleep(1)
                from droid_activities import ClickElement
                ClickElement.click_element("By.XPATH", "xpath",f"//i[contains(@class, 'mdi-cloud-download-outline')]",1,"Click Button",driver)
                from droid_activities import ClickElement
                ClickElement.click_element("By.XPATH", "xpath",f"//span[contains(@class, 'q-btn__content')]//span[normalize-space(text())='Clear All']",1,"Click Clear All",driver)
                time.sleep(2)
                from droid_activities import ClickElement
                ClickElement.click_element("By.XPATH", "xpath",f"//span[contains(@class, 'q-btn__content')]//i[contains(@class, 'mdi-cloud-download-outline')]",1,"Click Tasking Report",driver)
                from droid_activities import ClickElement
                ClickElement.click_element("By.XPATH", "xpath",f"//div[normalize-space(.)='Tasking Report']",1,"Click Date Range",driver)
                ClickElement.click_element("By.XPATH", "xpath",f"//div[contains(@class,'q-field__native') and normalize-space(text())='Beginning']",1,"Click Date Range",driver)
                from droid_activities import ClickElement
                from datetime import datetime
                currentdate = date_time.date_time('%m-%d-%Y', 'current', 0, "currentdate", "currentdate")
                dt = datetime.strptime(currentdate, "%m-%d-%Y")
                formatted =dt.strftime("%b %d").lower().replace(" 0", " ") 
                print(formatted)
                time.sleep(2)
                while True: #True
                    from droid_activities import ElementWait
                    Jan_exist = ElementWait.element_wait(driver, "By.XPATH", f"//div[@class='vc-title-wrapper']/button[@class='vc-title']/span[text()='January 2026']",3)
                    if Jan_exist == True: #range
                        from droid_activities import ClickElement
                        ClickElement.click_element("By.XPATH", "xpath",f"//div[@class='vc-day-content vc-focusable vc-focus vc-attr' and @aria-label='Thursday, Jan 1, 2026']",3,"Jan 01",driver)
                        break
                        #End If Jan_exist == True
                    else: #Else Start If Jan_exist == True
                        from droid_activities import ClickElement
                        ClickElement.click_element("By.XPATH", "xpath",f"//button[contains(@class,'vc-arrow') and contains(@class,'vc-prev')]",3,"Click Dropleft Button",driver)
                        #Else End If Jan_exist == True
                    #True End
                while True: #True
                    try: #Try Start
                        from droid_activities import ClickElement
                        ClickElement.click_element("By.XPATH", "xpath",f"//div[contains(@class,'vc-day') and contains(@class,'in-month')]//div[contains(@class,'vc-day-content') and contains(translate(@aria-label,'ABCDEFGHIJKLMNOPQRSTUVWXYZ','abcdefghijklmnopqrstuvwxyz'),'{formatted}')]",3,"Click Today Date",driver)
                        break
                        #Try End
                    except Exception as Er:
                        import traceback
                        Er = traceback.format_exc()
                        print(f"An error occurred: {Er}") #Except Start
                        from droid_activities import ClickElement
                        ClickElement.click_element("By.XPATH", "xpath",f"//button[contains(@class,'vc-arrow') and contains(@class,'vc-next')]",3,"Click Dropleft Button",driver)
                time.sleep(2)
                ClickElement.click_element("By.XPATH", "xpath",f"//div[contains(@class,'text-h6') and normalize-space(text())='Tasks Report']",1,"Click task ",driver)
                time.sleep(2)
                from droid_activities import ClickElement
                ClickElement.click_element("By.XPATH", "xpath",f"//div[@role='checkbox' and .//text()[normalize-space()='Include Completed Tasks']]",3,"Click Check Box",driver)
                ClickElement.click_element("By.XPATH", "xpath",f"//div[contains(@class,'q-field__inner')]//div[normalize-space(text())='Assignee']/ancestor::div[contains(@class,'q-field__inner')]",1,"Click Assignee",driver)
                ClickElement.click_element("By.XPATH", "xpath",f"//div[contains(@class,'q-field__control-container')]//input[@type='search' and @placeholder='Search']",1,"Click Search",driver)
                from droid_activities import TypeElement
                TypeElement.type_element("By.XPATH", "xpath",f"//div[contains(@class,'q-field__control-container')]//input[@type='search' and @placeholder='Search']","Jen Simpson",1,driver,"Type Patient Name")
                import time
                time.sleep(1)
                from droid_activities import ClickElement
                ClickElement.click_element("By.XPATH", "xpath",f"//div[contains(@class,'q-item__label') and normalize-space()='Jen Simpson']",1,"Click Jen Simpson",driver)
                time.sleep(1)
                ClickElement.click_element("By.XPATH", "xpath",f"//div[contains(@class,'q-field__control-container')]//input[@type='search' and @placeholder='Search']",1,"Click Search",driver)
                from droid_activities import emptyelement
                emptyelement.type_element("By.XPATH","xpath",f"//div[contains(@class,'q-field__control-container')]//input[@type='search' and @placeholder='Search']",1,driver,"Empty Search")
                from droid_activities import TypeElement
                TypeElement.type_element("By.XPATH", "xpath",f"//div[contains(@class,'q-field__control-container')]//input[@type='search' and @placeholder='Search']","Victoria Ballenger",1,driver,"Type Patient Name")
                import time
                time.sleep(1)
                from droid_activities import ClickElement
                ClickElement.click_element("By.XPATH", "xpath",f"//div[contains(@class,'q-item__label') and normalize-space()='Victoria Ballenger']",1,"Click Victoria Ballenger",driver)
                ClickElement.click_element("By.XPATH", "xpath",f"//div[contains(@class,'text-h6') and normalize-space(text())='Tasks Report']",3,"Click Task",driver)
                import time
                time.sleep(5)
                from datetime import datetime, timedelta
                import pandas as pd
                end_date = datetime.today()
                start_date = end_date - timedelta(days=6)
                start_str = start_date.strftime("%m-%d-%y")
                end_str = end_date.strftime("%m-%d-%y")
                filename = fr"C:\Users\DRD-DEV-0050\Downloads\Tasking Report - {start_str} to {end_str}.xlsx"
                from droid_activities import FileExists
                summaryfileexist = FileExists.file_exists(f'{filename}')
                if(summaryfileexist):
                    import os
                    os.rename(f'{filename}',fr"C:\Users\DRD-DEV-0050\Downloads\Tasking Report - {start_str} to {end_str}_1.xlsx")
                    time.sleep(3)
                ClickElement.click_element("By.XPATH", "xpath",f"//button[normalize-space(.)='Download']",3,"Click Download",driver)
                time.sleep(5)
                while(True):
                    from droid_activities import ElementWait
                    Download_exist = ElementWait.element_wait(driver, "By.XPATH", f"//span[contains(@class, 'q-btn__content')]//span[normalize-space()='Download']",5)
                    if(Download_exist):
                        ClickElement.click_element("By.XPATH", "xpath",f"//span[contains(@class, 'q-btn__content')]//span[normalize-space()='Download']",10,"Click Download",driver)
                        break
                    else:
                        print("Download Button not Exists")
                        time.sleep(5)
                time.sleep(5)
                #< --- Excel Filter Step ----->
                import time
                time.sleep(5)
                from datetime import datetime, timedelta
                import pandas as pd
                end_date = datetime.today()
                start_date = end_date - timedelta(days=6)
                start_str = start_date.strftime("%m-%d-%y")
                end_str = end_date.strftime("%m-%d-%y")
                filename = fr"C:\Users\DRD-DEV-0050\Downloads\Tasking Report - {start_str} to {end_str}.xlsx"
                print(filename)
                from droid_activities import date_time
                currentdate = date_time.date_time('%m-%d-%y', 'current', 0, "currentdate", "currentdate")
                from droid_activities import message_box_delay
                message_box_delay.show_timed_message_box('Starting the Dispatcher Process', 1)
                from droid_activities import Excelread_range
                dispatcherfile = Excelread_range.read_excelrange(filename,'Incomplete Tasks','A1:',"Read Patient inputfile")
                INPUT_EXCEL_FILE = filename
                OUTPUT_EXCEL_FILE = r"C:\RisePT\Input File\PatientCoordinationInputFile.xlsx"
                COLUMNS_TO_EXTRACT = [
                    "Task ID", "Task Title", "Task Created Date", "Task Created By",
                    "Task Assignee(s)", "Task Due Date", "Task Priority",
                    "Task Patient Name", "Task Patient Account Number"
                ]
                NPI_VALUE = "1851743009"
                try:
                    df = pd.read_excel(INPUT_EXCEL_FILE)
                    print(f"Successfully loaded '{INPUT_EXCEL_FILE}'. Original rows: {len(df)}")
                except FileNotFoundError:
                    print(f"Error: Input file '{INPUT_EXCEL_FILE}' not found.")
                    exit()
                except Exception as e:
                    print(f"An error occurred while reading the Excel file: {e}")
                    exit()
                if 'Task Title' in df.columns:
                    insurance_filter = df['Task Title'].str.contains(r'^(?:[1234]\s*sche.*eval.*text|discharge)$',case=False,regex=True,na=False)
                else:
                    print("Warning: 'Task Title' column not found. skipped insurance filter.")
                    insurance_filter = True
                filtered_df = df[insurance_filter].copy()
                print(f"Rows after filtration: {len(filtered_df)}")
                final_columns = [col for col in COLUMNS_TO_EXTRACT if col in filtered_df.columns]
                final_df = filtered_df[final_columns]
                final_df['NPI'] = NPI_VALUE
                try:
                    final_df.to_excel(OUTPUT_EXCEL_FILE, index=False)
                    print(f"\nFiltered data successfully saved to '{OUTPUT_EXCEL_FILE}'")
                except Exception as e:
                    print(f"Error saving filtered data to Excel: {e}")
                Success_DT = Excelread_range.read_excelrange(r"C:\RisePT\Input File\PatientCoordinationInputFile.xlsx",'Sheet1','A1:',"Read success records")
                success_count = int(len(Success_DT['Task Patient Account Number']))
                from droid_activities import textfileread
                dispatchermailfile = textfileread.read_textfile(r"C:\RisePT\Mail Templates\PatientCoordination_Dispatcher.txt","Tasking Report File")
                dispatchermailfile = dispatchermailfile.replace('{Current Date}', currentdate)
                dispatchermailfile = dispatchermailfile.replace('{queue_totalcount}', str(success_count))
                # from droid_activities import send_mail
                # tomail = ["Manikandan.c@droidal.com"]
                # ccmail = ["Manikandan.c@droidal.com"]
                # send_mail.send_email(filename,'risept@droidal.ai','kqf8vZzhkAPeiuvp8Y',tomail,ccmail,'Patient Coordination - RisePT Updating Patient Coordination Process - ' + currentdate.replace('-', '.')+ '.xlsx',dispatchermailfile,'smtp.office365.com',587)
                # <--------- Send Dispatcher mail ------------------->
                from openpyxl import load_workbook
                from datetime import datetime, date, timedelta
                import time
                import re
                time.sleep(5)
                end_date = datetime.today()
                start_date = end_date - timedelta(days=6)
                start_str = start_date.strftime("%m-%d-%y")
                end_str = end_date.strftime("%m-%d-%y")
                def parse_date(val):
                    if val is None:
                        return None
                    if isinstance(val, datetime):
                        return val
                    if isinstance(val, date):
                        return datetime.combine(val, datetime.min.time())
                    if isinstance(val, (int, float)):
                        try:
                            return datetime(1899, 12, 30) + timedelta(days=float(val))
                        except:
                            pass
                    val_str = str(val).strip()
                    if re.fullmatch(r"\d+(\.\d+)?", val_str):
                        try:
                            return datetime(1899, 12, 30) + timedelta(days=float(val_str))
                        except:
                            pass
                    formats = [
                        "%m-%d-%y", "%m-%d-%Y",
                        "%m/%d/%y", "%m/%d/%Y",
                        "%Y-%m-%d", "%Y-%m-%d %H:%M:%S",
                        "%d-%m-%Y", "%d/%m/%Y"
                    ]

                    for fmt in formats:
                        try:
                            return datetime.strptime(val_str, fmt)
                        except:
                            pass
                    try:
                        return datetime.fromisoformat(val_str.replace(" ", "T"))
                    except:
                        pass
                    return None
                file_path = fr"C:\Users\DRD-DEV-0050\Downloads\Tasking Report - {start_str} to {end_str}.xlsx"
                wb = load_workbook(file_path)
                ws = wb.active
                header = [cell.value for cell in ws[1]]
                date_col_index = header.index("Task Due Date")
                rows = list(ws.iter_rows(min_row=2, values_only=True))
                rows_with_dates = []
                for r in rows:
                    raw_date = r[date_col_index]
                    parsed_date = parse_date(raw_date)
                    rows_with_dates.append((parsed_date, r))
                rows_with_dates.sort(key=lambda x: (x[0] is None, x[0]))
                if ws.max_row > 1:
                    ws.delete_rows(2, ws.max_row - 1)
                for parsed, row_data in rows_with_dates:
                    ws.append(list(row_data))
                wb.save(file_path)
                print("✔ Sorted (by Task Due Date) & Saved Successfully:", file_path)
                print("\nSorted Output:")
                for parsed, row_data in rows_with_dates:
                    print(parsed)
                from droid_activities import date_time, textfileread, send_mail
                currentdate = date_time.date_time('%m-%d-%Y', 'current', 0, "currentdate", "currentdate")
                template = textfileread.read_textfile(r"C:\RisePT\Mail Templates\Send_TaskingReport_Mail.txt","summaryfile")
                mail_body = template.replace('{Current Date}', currentdate)
                tomail = ["victoria.ballenger@riseptnwa.com","jen.simpson@riseptnwa.com"]
                ccmail = ["Bosco.t@droidal.com","Manikandan.c@droidal.com","Praveen.r@droidal.ai"]
                send_mail.send_email(file_path,'risept@droidal.ai','kqf8vZzhkAPeiuvp8Y',tomail,ccmail,'RisePT Updating Patient Coordination Process - Tasking Report - ' + currentdate.replace('-', '.'),'RisePT_PatientCoordination_TaskingReport - ' + currentdate.replace('-', '.') + '.xlsx',mail_body,'smtp.office365.com',587)
                # < ------------------- Patients Menu -----------------># Need to command
                try:
                    Text2_filepath = r'C:\RisePT\Input File'+'\\'+'TextTask2_InputFile\\'+'RisePT_2texttask_inputReport - '+yesterday_Date.replace('-','.')+'.xlsx'
                    from droid_activities import FileExists
                    Text2fileexist = FileExists.file_exists(Text2_filepath)
                    if Text2fileexist == True: #range
                        try:
                            from droid_activities import Excelread_range
                            Texttask2_inputDT = Excelread_range.read_excelrange(Text2_filepath,'Sheet1', 'A1:', "Read Input File - inputDT")
                        except:
                            print(" Yester Day File not Exists")
                    else:
                        from droid_activities import date_time
                        yesterday_Date = date_time.date_time('%m-%d-%Y', 'before',3, "currentdate", "currentdate")
                        print(yesterday_Date)
                        Text2_filepath = r'C:\RisePT\Input File'+'\\'+'TextTask2_InputFile\\'+'RisePT_2texttask_inputReport - '+yesterday_Date.replace('-','.')+'.xlsx'
                        from droid_activities import Excelread_range
                        Texttask2_inputDT = Excelread_range.read_excelrange(Text2_filepath,'Sheet1', 'A1:', "Read Input File - inputDT")
                        # Update Excel
                    import openpyxl
                    def update_status(task_id, status, file_path=Text2_filepath):
                        wb = openpyxl.load_workbook(file_path)
                        ws = wb.active
                        for row in ws.iter_rows(min_row=2):
                            if str(row[1].value) == str(task_id):  # Column B = Task ID
                                row[6].value = status  # Column G = Status
                                break
                        wb.save(file_path)
                    Texttask2_inputkeys = list(Texttask2_inputDT.keys()); 
                    inputvalues = list(zip(*Texttask2_inputDT.values())); 
                    result = [dict(zip(Texttask2_inputkeys, value)) for value in inputvalues]
                    for index,currentitem in enumerate(result):
                        Accountnumber = str(currentitem['Task Patient Account Number'])#str
                        Patientname = str(currentitem['Task Patient Name']) #str
                        Tasktitle = str(currentitem['Task Title']) #str
                        TaskID = str(currentitem['Task ID'])
                        TaskAssingnee = str(currentitem['Task Assignee(s)'])
                        TaskStatus = str(currentitem['Status'])
                        if(TaskStatus == "Success"):
                            print(" Already Processed")
                            continue
                        from droid_activities import ElementWait
                        CloseTaskButton_exist = ElementWait.element_wait(driver, "By.XPATH", f"//button[contains(@class,'text-p-gray400')]//i[normalize-space(.)='close']/ancestor::button",10)
                        if(CloseTaskButton_exist):
                            print(" Close Task Button Exists for excption for empty task in the task list")
                            from droid_activities import ClickElement
                            ClickElement.click_element("By.XPATH", "xpath",f"//button[contains(@class,'text-p-gray400')]//i[normalize-space(.)='close']/ancestor::button",5,"Click Close Task",driver)
                        try:
                            import re
                            TaskNumber = re.findall(r'\d+', Tasktitle)[0]
                        except:
                            TaskNumber = Tasktitle
                        from droid_activities import windowhandle
                        switch_to_window_by_title(driver, "prompt")
                        time.sleep(5)
                        Is_PatientsnotFound = False
                        from droid_activities import ClickElement
                        ClickElement.click_element("By.XPATH", "xpath",f"//a[.//div[normalize-space()='Patients']]",1,"Patients Menu",driver)
                        from droid_activities import hoverElement
                        hoverElement.hover_element("By.XPATH", "xpath",f"//input[@*='Search patients'][@type='search']",1,"Patient Name Text Field",driver)
                        time.sleep(1)
                        from droid_activities import ClickElement
                        ClickElement.click_element("By.XPATH", "xpath",f"//input[@*='Search patients'][@type='search']",1,"patient Name text field",driver)
                        from droid_activities import emptyelement
                        emptyelement.type_element("By.XPATH","xpath",f"//input[@*='Search patients'][@type='search']",1,driver,"Patient Name Text Field")
                        import time
                        time.sleep(1)
                        from droid_activities import TypeElement
                        TypeElement.type_element("By.XPATH", "xpath",f"//input[@*='Search patients'][@type='search']",Accountnumber,1,driver,"Type Patient Name")
                        import time
                        time.sleep(3)
                        from droid_activities import ClickElement
                        ClickElement.click_element("By.XPATH", "xpath",f"//div[contains(@class, 'text-weight-medium') and contains(@class, 'text-subtitle1')]",1,"Patient Profile",driver)
                        import time
                        time.sleep(3)
                        from droid_activities import GetTextElement
                        Dateofbirth=GetTextElement.get_textElement("By.XPATH",f"//div[contains(@class,'p-text-body') and .//div[normalize-space(.)='Date of Birth']]//span[contains(@class,'text-p-gray600')]",1," Get DOB",driver)
                        print(Dateofbirth)
                        from datetime import datetime
                        BirthDate_1 = datetime.strptime(Dateofbirth, "%m/%d/%Y")
                        from droid_activities import GetTextElement
                        Mobileno = GetTextElement.get_textElement("By.XPATH",f"//div[normalize-space()='Mobile Phone']/following-sibling::div//span",1,"Mobile Number",driver)
                        print(Mobileno)
                        from droid_activities import hoverElement
                        hoverElement.hover_element("By.XPATH", "xpath",f"//div[contains(@class,'q-chip')][.//div[normalize-space()='Visits']]",1,"Visits",driver)
                        from droid_activities import ClickElement
                        ClickElement.click_element("By.XPATH", "xpath",f"//div[contains(@class,'q-chip')][.//div[normalize-space()='Visits']]",1,"Visits Menu",driver)
                        time.sleep(3)
                        import keyboard
                        from droid_activities import openbrowser
                        from droid_activities import windowhandle
                        windowhandle.window_handle(driver,1)
                        import time
                        time.sleep(3)
                        ClickElement.click_element("By.XPATH", "xpath",f"//a[.//span[normalize-space()='Contacts']]",1,"Click Contact",driver)
                        time.sleep(2)
                        Image_Path=r"C:\RisePT\Image Folder\Template_Close.png"
                        from droid_activities import CitrixImageExist
                        Msg_Template_Exists = CitrixImageExist.citrix_image_exist(Image_Path,10, 0.8)
                        if(Msg_Template_Exists):
                            print(" Msg Template not close because of some other issue kindly review this patients")
                            from droid_activities import HoverCoordinate
                            HoverCoordinate.hover_coordinates(822,122,"Hover")
                            time.sleep(2)
                            Image_Path=r"C:\RisePT\Image Folder\Template_Close.png";import subprocess, re;target_x, target_y = (int(m.group(1)), int(m.group(2))) if (m := re.search(r"target_x=(\d+), target_y=(\d+)", (out := subprocess.run(["python", r"C:\RisePT\Code Folder\Patients coordination\asa.py", Image_Path], capture_output=True, text=True)).stdout)) else (null, null);print(target_x);print(target_y)
                            from droid_activities import ClickCoordinate
                            ClickCoordinate.click_coordinates(target_x+15,target_y,"Click")
                            time.sleep(3)
                        ClickElement.click_element("By.XPATH", "xpath",f"//input[@placeholder='Search']",1,"Click Search Button",driver)
                        from droid_activities import emptyelement
                        emptyelement.type_element("By.XPATH","xpath",f"//input[@placeholder='Search']",1,driver,"Empty Search")
                        from droid_activities import TypeElement
                        TypeElement.type_element("By.XPATH", "xpath",f"//input[@placeholder='Search']",Patientname,1,driver,"Type Patient name")
                        time.sleep(3)
                        from droid_activities import ElementWait
                        Nodata_exist = ElementWait.element_wait(driver, "By.XPATH", f"//div[contains(@class,'frontend-1mipy11')]//p[normalize-space()='No data to display']",5)
                        if(Nodata_exist):
                            from droid_activities import excelappend
                            excelappend.append_excel('C:\\RisePT\\Daily Summary Folder'+'\\'+'RisePT_PatientCoordination_SummaryReport - '+currentdate.replace('-','.')+'.xlsx', [currentdate,TaskID,Tasktitle,Patientname,Dateofbirth,TaskAssingnee,Accountnumber,'Needs Attention','This Patient not Available in Weave Portal'], 'Sheet1')
                            time.sleep(2)
                            Is_PatientsnotFound = True
                            update_status(TaskID, "Failed")
                            continue
                        PatientRow_Count=1
                        Is_PatientExists = True
                        is_MSG_Exists = True
                        Is_Template = True
                        Is_break=False
                        WeavePatient_Exists = False
                        try:
                            while(PatientRow_Count <=7):
                                try:
                                    from droid_activities import ClickElement
                                    ClickElement.click_element("By.XPATH", "xpath",f"(//div[@aria-label='List row'])[{PatientRow_Count}]",1,"Click Patient",driver)
                                    Mobileno_2 = GetTextElement.get_textElement("By.XPATH",f"//li[.//span[normalize-space(text())='Mobile Number']]//p",3,"Mobile Number",driver)
                                    print(Mobileno_2)
                                    Dateofbirth_2 = GetTextElement.get_textElement("By.XPATH",f"//span[normalize-space()='Birthday']/following-sibling::p",3,"Birthday",driver)
                                    BirthDate_2 = datetime.strptime(Dateofbirth_2, "%B %d, %Y")
                                    print(BirthDate_2)
                                    if (Mobileno == Mobileno_2 and BirthDate_1 == BirthDate_2):
                                        print(" DOB and Mobile numbers are matching ")
                                        from droid_activities import ClickElement
                                        ClickElement.click_element("By.XPATH", "xpath",f"//button[@aria-label='Close panel'][1]",1,"Click Close",driver)
                                        Is_PatientExists = True
                                        break
                                    else:
                                        Is_PatientExists = False
                                        PatientRow_Count=PatientRow_Count+1
                                        continue                                    
                                except:
                                    import traceback
                                    Er = traceback.format_exc()
                                    print(f"An error occurred: {Er}") 
                                    Is_PatientExists = False
                                    break
                        except:
                            print(" Patients Not Found loop")
                        if(Is_PatientExists == False):
                            print("Patients Not Found")
                            from droid_activities import excelappend
                            excelappend.append_excel('C:\\RisePT\\Daily Summary Folder'+'\\'+'RisePT_PatientCoordination_SummaryReport - '+currentdate.replace('-','.')+'.xlsx', [currentdate,TaskID,Tasktitle,Patientname,Dateofbirth,TaskAssingnee,Accountnumber,'Needs Attention','This Patient not Available for Weave portal'], 'Sheet1')
                            time.sleep(2)
                            update_status(TaskID, "Failed")
                            Is_PatientsnotFound = True
                            continue
                        else:
                            try:
                                from droid_activities import ClickElement
                                ClickElement.click_element("By.XPATH", "xpath",f"//button[@aria-label='Close panel'][1]",1,"Click Close",driver)
                            except:
                                print("Already Closed")          
                            import time
                            time.sleep(2)
                            try:
                                from droid_activities import ClickElement
                                ClickElement.click_element("By.XPATH", "xpath",f"(//div[@aria-label='List row'])[{PatientRow_Count}]//button[contains(@data-trackingid,'global-action-button-message')]",3,"Click Msg Box",driver)
                                #driver.switch_to.default_content()
                                time.sleep(5)
                            except:
                                print(" Patient Message Not Available")
                                time.sleep(1)
                                from droid_activities import excelappend
                                excelappend.append_excel('C:\\RisePT\\Daily Summary Folder'+'\\'+'RisePT_PatientCoordination_SummaryReport - '+currentdate.replace('-','.')+'.xlsx', [currentdate,TaskID,Tasktitle,Patientname,Dateofbirth,TaskAssingnee,Accountnumber,'Needs Attention','The selected contact has no textable phone numbers'], 'Sheet1')
                                Is_PatientsnotFound = True
                                update_status(TaskID, "Failed")
                                continue
                                time.sleep(2)
                                is_MSG_Exists= False
                            Image_Path=r"C:\RisePT\Image Folder\Template_Close.png"
                            from droid_activities import CitrixImageExist
                            Msg_Template_Exists = CitrixImageExist.citrix_image_exist(Image_Path,10, 0.8)
                            if(Msg_Template_Exists == False):
                                print(" Msg Template not close because of some other issue kindly review this patients")
                                is_MSG_Exists= False   
                            if(is_MSG_Exists == False):
                                    print(" MSG Box not Available") 
                                    from droid_activities import excelappend
                                    excelappend.append_excel('C:\\RisePT\\Daily Summary Folder'+'\\'+'RisePT_PatientCoordination_SummaryReport - '+currentdate.replace('-','.')+'.xlsx', [currentdate,TaskID,Tasktitle,Patientname,Dateofbirth,TaskAssingnee,Accountnumber,'Needs Attention','The message template could not be accessed at this time'], 'Sheet1')
                                    Is_PatientsnotFound = True
                                    update_status(TaskID, "Failed")
                                    continue
                            else:
                                try:
                                    ClickElement.click_element("By.XPATH", "xpath",f"//button[contains(@id, 'r125')]",5,"Click msg option Button",driver)
                                except:
                                    try:
                                        from droid_activities import citriximageclick_simulate
                                        citriximageclick_simulate.citrix_image_click(r"C:\RisePT\Image Folder\template.png", 0.7)
                                        import time
                                        time.sleep(5)
                                    except: #Patients message not available
                                        print(" Patient Message Not Available")
                                        time.sleep(1)
                                        Is_Template=False
                                        from droid_activities import excelappend
                                        #excelappend.append_excel('C:\\RisePT\\Daily Summary Folder'+'\\'+'RisePT_PatientCoordination_SummaryReport - '+currentdate.replace('-','.')+'.xlsx', [currentdate,TaskID,Tasktitle,Patientname,Dateofbirth,TaskAssingnee,Accountnumber,'Needs Attention','The selected contact has no textable phone numbers'], 'Sheet1')
                                        time.sleep(2)
                                if(Is_Template == True):
                                    import time
                                    time.sleep(2)
                                    #driver.switch_to.default_content()
                                    # ClickElement.click_element("By.XPATH", "xpath",f"//button[normalize-space()='All Templates']",5,"Click Manual template",driver)
                                    time.sleep(2)
                                    ClickElement.click_element("By.XPATH", "xpath",f"//div[@class='frontend-i9gxme']//input[@placeholder='Search']",5,"Click Search Button",driver)
                                    NPC = "NPC: 2nd"
                                    from droid_activities import TypeElement
                                    TypeElement.type_element("By.XPATH", "xpath",f"//div[@class='frontend-i9gxme']//input[@placeholder='Search']",NPC,1,driver,"Type NPC: 1st")
                                    time.sleep(1)
                                    ClickElement.click_element("By.XPATH", "xpath",f"//p[contains(text(), '{NPC}')]",5,"Click paragraph",driver)
                                    time.sleep(3)
                                    try:
                                        ClickElement.click_element("By.XPATH", "xpath",f"//button[@data-trackingid='mini-chat-templates-menu-button']",5,"Click Template Icon",driver)
                                        time.sleep(3)
                                    except:
                                        from droid_activities import citriximageclick_simulate
                                        citriximageclick_simulate.citrix_image_click(r"C:\RisePT\Image Folder\Template_MSG.png", 0.7)
                                    import keyboard;
                                    import pyautogui
                                    pyautogui.hotkey('ctrl', 'a')
                                    time.sleep(1)
                                    pyautogui.hotkey('ctrl', 'c')
                                    time.sleep(1)
                                    import pyperclip
                                    text = pyperclip.paste()
                                    print(text)
                                    personalized_message = text.replace("___", TaskAssingnee.split()[0])
                                    print(personalized_message)
                                    name_2=Patientname
                                    personalized_message = personalized_message.replace("Preferred Name", name_2)
                                    print(personalized_message)
                                    time.sleep(3)
                                    import re
                                    trimmed = re.sub(r'\s+', ' ', personalized_message).strip()
                                    pyperclip.copy(trimmed)
                                    #lines = trimmed.split("\n")
                                    if("rise physical therapy" in trimmed.lower()):
                                        pyautogui.hotkey('ctrl', 'a')
                                        pyautogui.hotkey('ctrl', 'v')
                                        paste = pyperclip.paste()
                                        print(paste)
                                        time.sleep(1)
                                        try:
                                            ClickElement.click_element("By.XPATH", "xpath",f"//button[@data-trackingid='thread-send-button']",5,"Click Send Icon",driver)
                                            time.sleep(3)
                                        except:
                                            try:
                                                from droid_activities import citriximageclick_simulate
                                                citriximageclick_simulate.citrix_image_click(r"C:\RisePT\Image Folder\Send_Button.png", 0.8)
                                            except:
                                                time.sleep(3)
                                        #ClickElement.click_element("By.XPATH", "xpath",f"//button[@data-trackingid='chat-2.0-popup-inbox-close']",5,"Click Send Icon",driver)
                                        time.sleep(3)
                                        from droid_activities import HoverCoordinate
                                        HoverCoordinate.hover_coordinates(822,122,"Hover")
                                        try:
                                            Image_Path=r"C:\RisePT\Image Folder\Template_Close.png";import subprocess, re;target_x, target_y = (int(m.group(1)), int(m.group(2))) if (m := re.search(r"target_x=(\d+), target_y=(\d+)", (out := subprocess.run(["python", r"C:\RisePT\Code Folder\Patients coordination\asa.py", Image_Path], capture_output=True, text=True)).stdout)) else (null, null);print(target_x);print(target_y)
                                            from droid_activities import ClickCoordinate
                                            ClickCoordinate.click_coordinates(target_x+15,target_y,"Click")
                                        except:
                                            from droid_activities import messagebox
                                            messagebox.popup_message_box("Need to close")
                                    else:
                                        print(" NPC Msg Not Valid")
                                        from droid_activities import excelappend
                                        excelappend.append_excel('C:\\RisePT\\Daily Summary Folder'+'\\'+'RisePT_PatientCoordination_SummaryReport - '+currentdate.replace('-','.')+'.xlsx', [currentdate,TaskID,Tasktitle,Patientname,Dateofbirth,TaskAssingnee,Accountnumber,'Needs Attention','The NPC message template Are Not Valid'], 'Sheet1')
                                        update_status(TaskID, "Failed")
                                        Is_PatientsnotFound = True
                                        continue
                                else:
                                    print(" Already Send Msg Completed")                                 
                                time.sleep(5)
                                from droid_activities import excelappend
                                excelappend.append_excel('C:\\RisePT\\Daily Summary Folder'+'\\'+'RisePT_PatientCoordination_SummaryReport - '+currentdate.replace('-','.')+'.xlsx', [currentdate,TaskID,Tasktitle,Patientname,Dateofbirth,TaskAssingnee,Accountnumber,'Success','2 schedule eval text messages were sent successfully'], 'Sheet1')
                                update_status(TaskID, "Success")
                except Exception as e:
                    error_message = traceback.format_exc()
                    print("Error occurred:")
                    print(error_message)
                    try:
                        from droid_activities import excelappend
                        excelappend.append_excel('C:\\RisePT\\Daily Summary Folder'+'\\'+'RisePT_PatientCoordination_SummaryReport - '+currentdate.replace('-','.')+'.xlsx', [currentdate,"TaskID",Tasktitle,Patientname,Dateofbirth,TaskAssingnee,Accountnumber,'Needs Attention','2 schedule eval text messages Exception part'], 'Sheet1')
                    except:
                        print(" Excel Sheet not updated")
                    time.sleep(3)
                import pandas as pd
                df = pd.read_excel("C:\RisePT\Input File\PatientCoordinationInputFile.xlsx")
                df_sorted = df.sort_values(by="Task Title")  # sort by column
                df_sorted.to_excel("C:\RisePT\Input File\PatientCoordinationInputFile.xlsx", index=False)
                from droid_activities import Excelread_range
                inputDT = Excelread_range.read_excelrange(r"C:\RisePT\Input File\PatientCoordinationInputFile.xlsx",'Sheet1', 'A1:', "Read Input File - inputDT")
                inputkeys = list(inputDT.keys()); 
                inputvalues = list(zip(*inputDT.values())); 
                result = [dict(zip(inputkeys, value)) for value in inputvalues]
                for index,currentitem in enumerate(result):
                    try: #Try Start - Performer Process
                        Accountnumber = str(currentitem['Task Patient Account Number'])#str
                        Patientname = str(currentitem['Task Patient Name']) #str
                        Tasktitle = str(currentitem['Task Title']) #str
                        TaskID = str(currentitem['Task ID'])
                        TaskAssingnee = str(currentitem['Task Assignee(s)'])
                        print(Accountnumber)
                        print(Patientname)
                        print(Tasktitle)
                        if(is_Exception == True):
                            from droid_activities import windowhandle
                            switch_to_window_by_title(driver, "prompt")
                        time.sleep(4)
                        from droid_activities import ElementWait
                        CloseTaskButton_exist = ElementWait.element_wait(driver, "By.XPATH", f"//button[contains(@class,'text-p-gray400')]//i[normalize-space(.)='close']/ancestor::button",10)
                        if(CloseTaskButton_exist):
                            print(" Close Task Button Exists for excption for empty task in the task list")
                            from droid_activities import ClickElement
                            ClickElement.click_element("By.XPATH", "xpath",f"//button[contains(@class,'text-p-gray400')]//i[normalize-space(.)='close']/ancestor::button",5,"Click Close Task",driver)
                        try:
                            import re
                            TaskNumber = re.findall(r'\d+', Tasktitle)[0]
                        except:
                            TaskNumber = Tasktitle
                        try:
                            if("discharge" == Tasktitle.lower()):
                                print(" Discharege Patients")
                                from droid_activities import hoverElement
                                from droid_activities import ClickElement
                                ClickElement.click_element("By.XPATH", "xpath",f"//a[.//div[normalize-space()='Patients']]",1,"Patients Menu",driver)
                                time.sleep(1)
                                from droid_activities import ClickElement
                                ClickElement.click_element("By.XPATH", "xpath",f"//i[text()='search']/ancestor::div[contains(@class,'q-field')]//input",1,"patient Name text field",driver)
                                from droid_activities import emptyelement
                                emptyelement.type_element("By.XPATH","xpath",f"//i[text()='search']/ancestor::div[contains(@class,'q-field')]//input",1,driver,"Patient Name Text Field")
                                import time
                                time.sleep(1)
                                from droid_activities import TypeElement
                                TypeElement.type_element("By.XPATH", "xpath",f"//input[@*='Search patients'][@type='search']",Accountnumber,1,driver,"Type Patient Name")
                                import time
                                time.sleep(2)
                                from droid_activities import ClickElement
                                ClickElement.click_element("By.XPATH", "xpath",f"(//div[contains(@class,'patient')])[1]",1,"Patient Profile",driver)
                                time.sleep(3)
                                from droid_activities import GetTextElement 
                                Lastname= GetTextElement.get_textElement("By.XPATH",f"//div[normalize-space()='Date of Birth']/following::span[1]",1,"Get Last Name",driver)
                                print(Lastname)
                                Account_name = GetTextElement.get_textElement("By.XPATH",f"//div[normalize-space()='Account Number']/following::span[1]",1,"Get Account Number",driver)
                                print(Account_name)
                                from droid_activities import ClickElement
                                ClickElement.click_element("By.XPATH", "xpath",f"//div[text()='Visits']",1,"Visits Menu",driver)
                                from droid_activities import GetTextElement 
                                Get_future= GetTextElement.get_textElement("By.XPATH",f"//div[normalize-space(text())='Future']/following-sibling::div[normalize-space()]",1,"Get Future",driver)
                                print(Get_future)
                                Get_future=int(Get_future)
                                from droid_activities import ElementWait
                                NotCheckedIn_Exists = ElementWait.element_wait(driver, "By.XPATH", f"//tr[.//div[contains(text(),'Not Checked In')]]",10)
                                Get_All= GetTextElement.get_textElement("By.XPATH",f"//button[.//div[normalize-space()='All']]//div[contains(@class,'bg-p')]",1,"Get All",driver)
                                print(Get_All)
                                Get_All=int(Get_All)
                                from droid_activities import ElementWait
                                is_visit_missing = ElementWait.element_wait(driver, "By.XPATH", f"//i[@class='p-pa-xs q-icon text-p-red600 mdi mdi-alert-outline']",10)
                                from droid_activities import ElementWait
                                visit_missing = ElementWait.element_wait(driver, "By.XPATH", f"//i[@class='p-pa-xs q-icon text-p-red600 mdi mdi-alert-outline']",5)
                                # if(Get_All >= 0 or is_visit_missing == True ):  
                                if(Get_future <= 0 or NotCheckedIn_Exists == False):  
                                    from droid_activities import ClickElement
                                    ClickElement.click_element("By.XPATH", "xpath",f"//div[text()='Cases']",1,"Cases Menu",driver)
                                    from droid_activities import ElementWait
                                    is_Discharged = ElementWait.element_wait(driver, "By.XPATH", f"//button[.//span[normalize-space()='Discharge Case']]",10)
                                    if(is_Discharged != True):
                                        print(" This Patients already Discharged")
                                        time.sleep(2)
                                        from droid_activities import ClickElement
                                        ClickElement.click_element("By.XPATH", "xpath",f"(//button[.//i[contains(@class,'mdi-checkbox-marked-circle-plus-outline')]])[2]",4,"Click Task Button",driver)  
                                        try:
                                            from droid_activities import ClickElement
                                            ClickElement.click_element("By.XPATH", "xpath",f"//div[normalize-space()='Discharge']/ancestor::div[contains(@class,'ticketModalRow')]//button[.//div[normalize-space()='Mark Complete']]",4,"Click Task Complete",driver)
                                            from droid_activities import ClickElement
                                            ClickElement.click_element("By.XPATH", "xpath",f"//button[contains(@class,'text-p-gray400')]//i[normalize-space(.)='close']/ancestor::button",4,"Click Save Task",driver)
                                        except:
                                            print(" No response task not available")
                                        from droid_activities import excelappend
                                        excelappend.append_excel('C:\\RisePT\\Daily Summary Folder'+'\\'+'RisePT_PatientCoordination_SummaryReport - '+currentdate.replace('-','.')+'.xlsx', [currentdate,TaskID,"discharge",Patientname,Lastname,"N/A",Account_name,'Needs Attention','This patient Already discharged'], 'Sheet1')
                                        continue  
                                    else:
                                        print(" Its Not Already Discharged ") 
                                    Get_Referring_Provider=""
                                    try:
                                        hoverElement.hover_element("By.XPATH", "xpath",f"//div[normalize-space(text())='Referring Provider (PRIMARY)'][1]",1,"Referring Provider (PRIMARY)",driver)
                                        from droid_activities import GetTextElement 
                                        Get_Referring_Provider= GetTextElement.get_textElement("By.XPATH",f"//div[normalize-space(text())='Referring Provider (PRIMARY)']/following::span[@class='text-p-gray600'][1]",1,"Get Referring_Provider",driver)
                                        print(Get_Referring_Provider)
                                        parts = [p.strip() for p in Get_Referring_Provider.split(",")]
                                        if len(parts) == 2:
                                            last, first = parts
                                            Referring_Provider = f"{first} {last}"
                                        elif len(parts) == 3:
                                            last, md, first = parts
                                            Referring_Provider = f"{first} {last}"
                                        print(Referring_Provider)
                                        time.sleep(3)
                                    except:
                                        print(" Not Found Referring Provider ")
                                    if (Get_Referring_Provider != ""):
                                        try:
                                            from droid_activities import hoverElement
                                            hoverElement.hover_element("By.XPATH", "xpath",f"//div[@class='ellipsis' and normalize-space(.)='Files']",1,"Files Menu",driver)
                                            from droid_activities import ClickElement
                                            ClickElement.click_element("By.XPATH", "xpath",f"//div[@class='ellipsis' and normalize-space(.)='Files']",1,"Files Menu",driver)
                                            import time
                                            time.sleep(1)
                                            ClickElement.click_element("By.XPATH", "xpath",f"//a[normalize-space(text())='All Files']",7,"Click All Files",driver)
                                            time.sleep(3)
                                            try:
                                                from droid_activities import hoverElement
                                                hoverElement.hover_element("By.XPATH", "xpath",f"//div[contains(@class, 'q-expansion-item')] [.//div[contains(normalize-space(.), 'Referral')]] //button[.//i[text()='more_vert']]",1,"Referral Menu",driver)
                                                ClickElement.click_element("By.XPATH", "xpath",f"//div[contains(@class, 'q-expansion-item')] [.//div[contains(normalize-space(.), 'Referral')]] //button[.//i[text()='more_vert']]",7,"Click Referral",driver)
                                            except:
                                                try:
                                                    from droid_activities import hoverElement
                                                    hoverElement.hover_element("By.XPATH", "xpath",f"//div[contains(@class, 'q-expansion-item')] [.//div[contains(normalize-space(.), 'REF')]] //button[.//i[text()='more_vert']]",1,"Referral Menu",driver)
                                                    ClickElement.click_element("By.XPATH", "xpath",f"//div[contains(@class, 'q-expansion-item')] [.//div[contains(normalize-space(.), 'REF')]] //button[.//i[text()='more_vert']]",7,"Click Referral",driver)
                                                except:
                                                    try:
                                                        from droid_activities import hoverElement
                                                        hoverElement.hover_element("By.XPATH", "xpath",f"//div[contains(@class, 'q-expansion-item')] [.//div[contains(normalize-space(.), 'ref')]] //button[.//i[text()='more_vert']]",1,"Referral Menu",driver)
                                                        ClickElement.click_element("By.XPATH", "xpath",f"//div[contains(@class, 'q-expansion-item')] [.//div[contains(normalize-space(.), 'ref')]] //button[.//i[text()='more_vert']]",7,"Click Referral",driver)
                                                    except:
                                                        from droid_activities import hoverElement
                                                        hoverElement.hover_element("By.XPATH", "xpath",f"//div[contains(@class, 'q-expansion-item')] [.//div[contains(normalize-space(.), 'Doctor Referrel')]] //button[.//i[text()='more_vert']]",1,"Referral Menu",driver)
                                                        ClickElement.click_element("By.XPATH", "xpath",f"//div[contains(@class, 'q-expansion-item')] [.//div[contains(normalize-space(.), 'Doctor Referrel')]] //button[.//i[text()='more_vert']]",7,"Click Referral",driver)
                                            ClickElement.click_element("By.XPATH", "xpath",f"//button[.//span[normalize-space(text())='Fax']]",7,"Click Fax",driver)
                                            ClickElement.click_element("By.XPATH", "xpath",f"//div[contains(@class, 'q-field__control')] //div[normalize-space(text())='From Facility']/ancestor::div[contains(@class, 'q-field__control')]",7,"Click West Selected",driver)
                                            ClickElement.click_element("By.XPATH", "xpath",f"//div[@role='option']//div[normalize-space()='West']",7,"Click West",driver) 
                                            from droid_activities import ClickElement
                                            ClickElement.click_element("By.XPATH", "xpath",f"//label[.//div[contains(text(),'To Number')]]//i[text()='arrow_drop_down']",2,"Cick DropDown",driver)
                                            try:
                                                from droid_activities import ClickElement
                                                ClickElement.click_element("By.XPATH", "xpath",f"//div[contains(@class,'p-select__option-descriptor_gray') and contains(., '{Referring_Provider}')]",3,"Cick DropDown",driver)
                                                time.sleep(3)
                                                ClickElement.click_element("By.XPATH", "xpath",f"//textarea[@aria-label='Message']",7,"Click message",driver)
                                                Temp_message = """We received a referral to schedule this patient for an evaluation and made four attempts
                                                to contact them, but didn’t get a response. I'm sending the referral back to your office for now.
                                                If the patient reaches out to us, we’re happy to get them scheduled.
                                                If you have any questions, feel free to call us at 479-318-0017. Thank you!"""
                                                print(Temp_message) # Check Message
                                                import re
                                                clean_message = re.sub(r"\s+", " ", Temp_message).strip()
                                                from droid_activities import TypeElement
                                                TypeElement.type_element("By.XPATH", "xpath",f"//textarea[@aria-label='Message']",clean_message,1,driver,"Type template Text")
                                                time.sleep(3)
                                                ClickElement.click_element("By.XPATH", "xpath",f"//button[.//span[normalize-space(text())='Send Fax']]",7,"Click Send Fax",driver)
                                            except:
                                                from droid_activities import ClickCoordinate
                                                ClickCoordinate.click_coordinates(1814,535,"Click")
                                                from droid_activities import ClickCoordinate
                                                ClickCoordinate.click_coordinates(1814,535,"Click")
                                                print(" refering provider not available")
                                        except:
                                            print(" Files not found")
                                    from droid_activities import hoverElement
                                    hoverElement.hover_element("By.XPATH", "xpath",f"//div[text()='Cases']",3,"Case Menu",driver)
                                    ClickElement.click_element("By.XPATH", "xpath",f"//div[text()='Cases']",3,"Click Case",driver)
                                    ClickElement.click_element("By.XPATH", "xpath",f"//button[.//span[normalize-space(text())='Discharge Case']]",3,"Click Discharge Case",driver)
                                    ClickElement.click_element("By.XPATH", "xpath",f"//input[@aria-label='Discharge Date']",7,"Click Discharge Date",driver)
                                    from droid_activities import date_time
                                    Discharge_Date = date_time.date_time('%m/%d/%Y', 'current',0, "currentdate","currentdate")
                                    print(Discharge_Date)
                                    from droid_activities import TypeElement
                                    TypeElement.type_element("By.XPATH", "xpath",f"//input[@aria-label='Discharge Date']",Discharge_Date,3,driver,"Type Discharge Date")
                                    try:
                                        while(True):
                                            ClickElement.click_element("By.XPATH", "xpath",f"//div[normalize-space()='Discharge Reason']/ancestor::div[contains(@class,'q-field__control')]//i[contains(@class,'q-select__dropdown-icon')]",3,"Click Discharge Reason",driver)
                                            time.sleep(2)
                                            from droid_activities import ElementWait
                                            CasenotUsed_Exists = ElementWait.element_wait(driver,"By.XPATH",f"//div[@role='option' and normalize-space()='Case not used']",5)
                                            if(CasenotUsed_Exists):
                                                ClickElement.click_element("By.XPATH", "xpath",f"//div[@role='option' and normalize-space()='Case not used']",3,"Click Case not used",driver)
                                                from droid_activities import ElementWait
                                                SelectedCasenotUsed_Exists= ElementWait.element_wait(driver,"By.XPATH",f"//input[@aria-label='Discharge Reason' and @value='Case not used']",3)
                                                if(SelectedCasenotUsed_Exists):
                                                    ClickElement.click_element("By.XPATH", "xpath",f"//div[contains(@class,'q-ml-md') and .//span[normalize-space()='Discharge Case']][1]",3,"Click Discharge Case",driver)
                                                    break
                                    except:
                                        try:
                                            print("Case not used are exception")
                                            ClickElement.click_element("By.XPATH", "xpath",f"//div[normalize-space()='Discharge Reason']/ancestor::div[contains(@class,'q-field__control')]//i[contains(@class,'q-select__dropdown-icon')]",3,"Click Discharge Reason",driver)
                                            time.sleep(2)
                                            ClickElement.click_element("By.XPATH", "xpath",f"//div[@role='option' and normalize-space()='Case not used']",3,"Click Case not used",driver)
                                            time.sleep(3)
                                            ClickElement.click_element("By.XPATH", "xpath",f"//div[contains(@class,'q-ml-md') and .//span[normalize-space()='Discharge Case']][1]",3,"Click Discharge Case",driver)
                                        except:
                                            from droid_activities import excelappend
                                            excelappend.append_excel('C:\\RisePT\\Daily Summary Folder'+'\\'+'RisePT_PatientCoordination_SummaryReport - '+currentdate.replace('-','.')+'.xlsx', [currentdate,"N/A","Discharge",Last_Fname+" "+Last_Lname,Last_DOB_4th,"N/A","N/A",'Needs Attention','Case not used Exception Occurs'], 'Sheet1')
                                            continue
                                    time.sleep(2)
                                    from droid_activities import ClickElement
                                    ClickElement.click_element("By.XPATH", "xpath",f"(//button[.//i[contains(@class,'mdi-checkbox-marked-circle-plus-outline')]])[2]",4,"Click Task Button",driver)  
                                    try:
                                        from droid_activities import ClickElement
                                        ClickElement.click_element("By.XPATH", "xpath",f"//div[normalize-space()='{Tasktitle}']/ancestor::div[contains(@class,'ticketModalRow')]//button[.//div[normalize-space()='Mark Complete']]",4,"Click Task Complete",driver)
                                        from droid_activities import ClickElement
                                        ClickElement.click_element("By.XPATH", "xpath",f"//button[contains(@class,'text-p-gray400')]//i[normalize-space(.)='close']/ancestor::button",4,"Click Save Task",driver)
                                    except:
                                        print(" No response task not available")
                                    from droid_activities import excelappend
                                    excelappend.append_excel('C:\\RisePT\\Daily Summary Folder'+'\\'+'RisePT_PatientCoordination_SummaryReport - '+currentdate.replace('-','.')+'.xlsx', [currentdate,TaskID,"Discharge",Patientname,Lastname,"N/A",Account_name,'Success','This patient has been successfully discharged'], 'Sheet1')
                                    continue
                                else:
                                    print("Visits are not available")
                                    from droid_activities import excelappend
                                    excelappend.append_excel('C:\\RisePT\\Daily Summary Folder'+'\\'+'RisePT_PatientCoordination_SummaryReport - '+currentdate.replace('-','.')+'.xlsx', [currentdate,TaskID,"Discharge",Patientname,Lastname,"N/A",Account_name,'Needs Attention','Future appointments are available for this patient'], 'Sheet1')
                                    continue
                        except:
                            print(" Records Finish")
                            import traceback
                            Er = traceback.format_exc()
                            print(f"An error occurred: {Er}") 
                            from droid_activities import excelappend
                            excelappend.append_excel('C:\\RisePT\\Daily Summary Folder'+'\\'+'RisePT_PatientCoordination_SummaryReport - '+currentdate.replace('-','.')+'.xlsx', [currentdate,TaskID,"Discharge",Patientname,Lastname,"N/A",Account_name,'Needs Attention','This patient needs attention for further review'], 'Sheet1')
                            # from droid_activities import messagebox
                            # messagebox.popup_message_box("End Of Exception")
                            continue
                        from droid_activities import ClickElement
                        ClickElement.click_element("By.XPATH", "xpath",f"//a[.//div[normalize-space()='Patients']]",1,"Patients Menu",driver)
                        from droid_activities import hoverElement
                        hoverElement.hover_element("By.XPATH", "xpath",f"//input[@*='Search patients'][@type='search']",1,"Patient Name Text Field",driver)
                        time.sleep(1)
                        from droid_activities import ClickElement
                        ClickElement.click_element("By.XPATH", "xpath",f"//input[@*='Search patients'][@type='search']",1,"patient Name text field",driver)
                        from droid_activities import emptyelement
                        emptyelement.type_element("By.XPATH","xpath",f"//input[@*='Search patients'][@type='search']",1,driver,"Patient Name Text Field")
                        import time
                        time.sleep(1)
                        from droid_activities import TypeElement
                        TypeElement.type_element("By.XPATH", "xpath",f"//input[@*='Search patients'][@type='search']",Accountnumber,1,driver,"Type Patient Name")
                        import time
                        time.sleep(3)
                        from droid_activities import ClickElement
                        ClickElement.click_element("By.XPATH", "xpath",f"//div[contains(@class, 'text-weight-medium') and contains(@class, 'text-subtitle1')]",1,"Patient Profile",driver)
                        import time
                        time.sleep(3)
                        from droid_activities import GetTextElement
                        Dateofbirth=GetTextElement.get_textElement("By.XPATH",f"//div[contains(@class,'p-text-body') and .//div[normalize-space(.)='Date of Birth']]//span[contains(@class,'text-p-gray600')]",1," Get DOB",driver)
                        print(Dateofbirth)
                        # from droid_activities import date_time
                        # BirthDate_1 = datetime.strptime(Dateofbirth, "%m/%d/%Y")
                        from datetime import datetime
                        BirthDate_1 = datetime.strptime(Dateofbirth, "%m/%d/%Y")
                        from droid_activities import GetTextElement
                        Mobileno = GetTextElement.get_textElement("By.XPATH",f"//div[normalize-space()='Mobile Phone']/following-sibling::div//span",1,"Mobile Number",driver)
                        print(Mobileno)
                        from droid_activities import hoverElement
                        hoverElement.hover_element("By.XPATH", "xpath",f"//div[contains(@class,'q-chip')][.//div[normalize-space()='Visits']]",1,"Visits",driver)
                        from droid_activities import ClickElement
                        ClickElement.click_element("By.XPATH", "xpath",f"//div[contains(@class,'q-chip')][.//div[normalize-space()='Visits']]",1,"Visits Menu",driver)
                        time.sleep(3)
                        from droid_activities import ClickElement
                        ClickElement.click_element("By.XPATH", "xpath",f"(//button[.//i[contains(@class,'mdi-checkbox-marked-circle-plus-outline')]])[2]",4,"Click Task Button",driver)
                        time.sleep(6)
                        from droid_activities import ClickElement
                        ClickElement.click_element("By.XPATH", "xpath",f"//div[.//div[text()='Task List']]//button[.//i[text()='close']]",4,"Click Close Button",driver)
                        time.sleep(3)
                        #End If - Home Page Exist
                    #Try End - Launch an Login EMR Portal                
                        # Weave Part of this process: ## new one
                        if (TaskNumber == "2"):
                            print("2 Text Task")
                            from droid_activities import excelappend
                            excelappend.append_excel('C:\\RisePT\\Input File\\TextTask2_InputFile'+'\\'+'RisePT_2texttask_inputReport - '+currentdate.replace('-','.')+'.xlsx', [currentdate,TaskID,Tasktitle,TaskAssingnee,Patientname,Accountnumber,"New"], 'Sheet1')
                            time.sleep(2)
                        else:
                            import keyboard
                            from droid_activities import openbrowser
                            from droid_activities import windowhandle
                            windowhandle.window_handle(driver,1)
                            import time
                            time.sleep(3)
                            ClickElement.click_element("By.XPATH", "xpath",f"//a[.//span[normalize-space()='Contacts']]",1,"Click Contact",driver)
                            time.sleep(2)
                            Image_Path=r"C:\RisePT\Image Folder\Template_Close.png"
                            from droid_activities import CitrixImageExist
                            Msg_Template_Exists = CitrixImageExist.citrix_image_exist(Image_Path,10, 0.8)
                            if(Msg_Template_Exists):
                                print(" Msg Template not close because of some other issue kindly review this patients")
                                from droid_activities import HoverCoordinate
                                HoverCoordinate.hover_coordinates(822,122,"Hover")
                                time.sleep(2)
                                Image_Path=r"C:\RisePT\Image Folder\Template_Close.png";import subprocess, re;target_x, target_y = (int(m.group(1)), int(m.group(2))) if (m := re.search(r"target_x=(\d+), target_y=(\d+)", (out := subprocess.run(["python", r"C:\RisePT\Code Folder\Patients coordination\asa.py", Image_Path], capture_output=True, text=True)).stdout)) else (null, null);print(target_x);print(target_y)
                                from droid_activities import ClickCoordinate
                                ClickCoordinate.click_coordinates(target_x+15,target_y,"Click")
                                time.sleep(3)
                            ClickElement.click_element("By.XPATH", "xpath",f"//input[@placeholder='Search']",1,"Click Search Button",driver)
                            from droid_activities import emptyelement
                            emptyelement.type_element("By.XPATH","xpath",f"//input[@placeholder='Search']",1,driver,"Empty Search")
                            from droid_activities import TypeElement
                            TypeElement.type_element("By.XPATH", "xpath",f"//input[@placeholder='Search']",Patientname,1,driver,"Type Patient name")
                            time.sleep(3)
                            from droid_activities import ElementWait
                            Nodata_exist = ElementWait.element_wait(driver, "By.XPATH", f"//div[contains(@class,'frontend-1mipy11')]//p[normalize-space()='No data to display']",5)
                            if(Nodata_exist):
                                from droid_activities import excelappend
                                excelappend.append_excel('C:\\RisePT\\Daily Summary Folder'+'\\'+'RisePT_PatientCoordination_SummaryReport - '+currentdate.replace('-','.')+'.xlsx', [currentdate,TaskID,Tasktitle,Patientname,Dateofbirth,TaskAssingnee,Accountnumber,'Needs Attention','This Patient not Available in Weave Portal'], 'Sheet1')
                                time.sleep(2)
                                continue
                            PatientRow_Count=1
                            Is_PatientExists = True
                            is_MSG_Exists = True
                            Is_Template = True
                            Is_break=False
                            WeavePatient_Exists = False
                            try:
                                while(PatientRow_Count <=7):
                                    try:
                                        from droid_activities import ClickElement
                                        ClickElement.click_element("By.XPATH", "xpath",f"(//div[@aria-label='List row'])[{PatientRow_Count}]",1,"Click Patient",driver)
                                        Mobileno_2 = GetTextElement.get_textElement("By.XPATH",f"//li[.//span[normalize-space(text())='Mobile Number']]//p",3,"Mobile Number",driver)
                                        print(Mobileno_2)
                                        Dateofbirth_2 = GetTextElement.get_textElement("By.XPATH",f"//span[normalize-space()='Birthday']/following-sibling::p",3,"Birthday",driver)
                                        BirthDate_2 = datetime.strptime(Dateofbirth_2, "%B %d, %Y")
                                        print(BirthDate_2)
                                        if (Mobileno == Mobileno_2 and BirthDate_1 == BirthDate_2):
                                            print(" DOB and Mobile numbers are matching ")
                                            from droid_activities import ClickElement
                                            ClickElement.click_element("By.XPATH", "xpath",f"//button[@aria-label='Close panel'][1]",1,"Click Close",driver)
                                            Is_PatientExists = True
                                            break
                                        else:
                                            Is_PatientExists = False
                                            PatientRow_Count=PatientRow_Count+1
                                            continue                                    
                                    except:
                                        import traceback
                                        Er = traceback.format_exc()
                                        print(f"An error occurred: {Er}") 
                                        Is_PatientExists = False
                                        break
                            except:
                                print(" Patients Not Found loop")
                            if(Is_PatientExists == False):
                                print("Patients Not Found")
                                from droid_activities import excelappend
                                excelappend.append_excel('C:\\RisePT\\Daily Summary Folder'+'\\'+'RisePT_PatientCoordination_SummaryReport - '+currentdate.replace('-','.')+'.xlsx', [currentdate,TaskID,Tasktitle,Patientname,Dateofbirth,TaskAssingnee,Accountnumber,'Needs Attention','This Patient not Available for Weave portal'], 'Sheet1')
                                time.sleep(2)
                                continue
                            else:
                                try:
                                    from droid_activities import ClickElement
                                    ClickElement.click_element("By.XPATH", "xpath",f"//button[@aria-label='Close panel'][1]",1,"Click Close",driver)
                                except:
                                    print("Already Closed")          
                                import time
                                time.sleep(2)
                                try:
                                    from droid_activities import ClickElement
                                    ClickElement.click_element("By.XPATH", "xpath",f"(//div[@aria-label='List row'])[{PatientRow_Count}]//button[contains(@data-trackingid,'global-action-button-message')]",3,"Click Msg Box",driver)
                                    #driver.switch_to.default_content()
                                    time.sleep(5)
                                except:
                                    print(" Patient Message Not Available")
                                    time.sleep(1)
                                    from droid_activities import excelappend
                                    excelappend.append_excel('C:\\RisePT\\Daily Summary Folder'+'\\'+'RisePT_PatientCoordination_SummaryReport - '+currentdate.replace('-','.')+'.xlsx', [currentdate,TaskID,Tasktitle,Patientname,Dateofbirth,TaskAssingnee,Accountnumber,'Needs Attention','The selected contact has no textable phone numbers'], 'Sheet1')
                                    continue
                                    time.sleep(2)
                                    is_MSG_Exists= False
                                Image_Path=r"C:\RisePT\Image Folder\Template_Close.png"
                                from droid_activities import CitrixImageExist
                                Msg_Template_Exists = CitrixImageExist.citrix_image_exist(Image_Path,10, 0.8)
                                if(Msg_Template_Exists == False):
                                    print(" Msg Template not close because of some other issue kindly review this patients")
                                    is_MSG_Exists= False   
                                if(is_MSG_Exists == False):
                                        print(" MSG Box not Available") 
                                        from droid_activities import excelappend
                                        excelappend.append_excel('C:\\RisePT\\Daily Summary Folder'+'\\'+'RisePT_PatientCoordination_SummaryReport - '+currentdate.replace('-','.')+'.xlsx', [currentdate,TaskID,Tasktitle,Patientname,Dateofbirth,TaskAssingnee,Accountnumber,'Needs Attention','The message template could not be accessed at this time'], 'Sheet1')
                                        continue
                                else:
                                    try:
                                        ClickElement.click_element("By.XPATH", "xpath",f"//button[contains(@id, 'r125')]",5,"Click msg option Button",driver)
                                    except:
                                        try:
                                            from droid_activities import citriximageclick_simulate
                                            citriximageclick_simulate.citrix_image_click(r"C:\RisePT\Image Folder\template.png", 0.7)
                                            import time
                                            time.sleep(5)
                                        except: #Patients message not available
                                            print(" Patient Message Not Available")
                                            time.sleep(1)
                                            Is_Template=False
                                            from droid_activities import excelappend
                                            #excelappend.append_excel('C:\\RisePT\\Daily Summary Folder'+'\\'+'RisePT_PatientCoordination_SummaryReport - '+currentdate.replace('-','.')+'.xlsx', [currentdate,TaskID,Tasktitle,Patientname,Dateofbirth,TaskAssingnee,Accountnumber,'Needs Attention','The selected contact has no textable phone numbers'], 'Sheet1')
                                            time.sleep(2)
                                    if(Is_Template == True):
                                        import time
                                        time.sleep(2)
                                        #driver.switch_to.default_content()
                                        # ClickElement.click_element("By.XPATH", "xpath",f"//button[normalize-space()='All Templates']",5,"Click Manual template",driver)
                                        time.sleep(2)
                                        ClickElement.click_element("By.XPATH", "xpath",f"//div[@class='frontend-i9gxme']//input[@placeholder='Search']",5,"Click Search Button",driver)
                                        if(TaskNumber =="1"):
                                            NPC = "NPC: 1st"
                                        elif(TaskNumber == "2"):
                                            NPC = "NPC: 2nd"
                                        elif(TaskNumber == "3"):
                                            NPC = "NPC: 3rd"
                                        elif(TaskNumber == "4"):
                                            NPC = "NPC: 4th"
                                        from droid_activities import TypeElement
                                        TypeElement.type_element("By.XPATH", "xpath",f"//div[@class='frontend-i9gxme']//input[@placeholder='Search']",NPC,1,driver,"Type NPC: 1st")
                                        time.sleep(1)
                                        ClickElement.click_element("By.XPATH", "xpath",f"//p[contains(text(), '{NPC}')]",5,"Click paragraph",driver)
                                        time.sleep(3)
                                        try:
                                            ClickElement.click_element("By.XPATH", "xpath",f"//button[@data-trackingid='mini-chat-templates-menu-button']",5,"Click Template Icon",driver)
                                            time.sleep(3)
                                        except:
                                            if(TaskNumber =="1"):
                                                from droid_activities import citriximageclick_simulate
                                                citriximageclick_simulate.citrix_image_click(r"C:\RisePT\Image Folder\Template_MSG_01.png", 0.7)
                                            else:
                                                from droid_activities import citriximageclick_simulate
                                                citriximageclick_simulate.citrix_image_click(r"C:\RisePT\Image Folder\Template_MSG.png", 0.7)
                                        import keyboard;
                                        import pyautogui
                                        pyautogui.hotkey('ctrl', 'a')
                                        time.sleep(1)
                                        pyautogui.hotkey('ctrl', 'c')
                                        time.sleep(1)
                                        import pyperclip
                                        text = pyperclip.paste()
                                        print(text)
                                        if(TaskNumber =="1"):
                                            personalized_message = text.replace("[Name]", TaskAssingnee.split()[0])
                                        else:
                                            personalized_message = text.replace("___", TaskAssingnee.split()[0])
                                        print(personalized_message)
                                        name_2=Patientname
                                        personalized_message = personalized_message.replace("Preferred Name", name_2)
                                        print(personalized_message)
                                        time.sleep(3)
                                        import re
                                        trimmed = re.sub(r'\s+', ' ', personalized_message).strip()
                                        pyperclip.copy(trimmed)
                                        #lines = trimmed.split("\n")
                                        if("rise physical therapy" in trimmed.lower()):
                                            pyautogui.hotkey('ctrl', 'a')
                                            pyautogui.hotkey('ctrl', 'v')
                                            paste = pyperclip.paste()
                                            print(paste)
                                            time.sleep(1)
                                            try:
                                                ClickElement.click_element("By.XPATH", "xpath",f"//button[@data-trackingid='thread-send-button']",5,"Click Send Icon",driver)
                                                time.sleep(3)
                                            except:
                                                try:
                                                    from droid_activities import citriximageclick_simulate
                                                    citriximageclick_simulate.citrix_image_click(r"C:\RisePT\Image Folder\Send_Button.png", 0.8)
                                                except:
                                                    time.sleep(3)
                                            #ClickElement.click_element("By.XPATH", "xpath",f"//button[@data-trackingid='chat-2.0-popup-inbox-close']",5,"Click Send Icon",driver)
                                            time.sleep(3)
                                            from droid_activities import HoverCoordinate
                                            HoverCoordinate.hover_coordinates(822,122,"Hover")
                                            time.sleep(1)
                                            from droid_activities import HoverCoordinate
                                            HoverCoordinate.hover_coordinates(1721,364,"Hover")
                                            try:
                                                Image_Path=r"C:\RisePT\Image Folder\Template_Close.png";import subprocess, re;target_x, target_y = (int(m.group(1)), int(m.group(2))) if (m := re.search(r"target_x=(\d+), target_y=(\d+)", (out := subprocess.run(["python", r"C:\RisePT\Code Folder\Patients coordination\asa.py", Image_Path], capture_output=True, text=True)).stdout)) else (null, null);print(target_x);print(target_y)
                                                from droid_activities import ClickCoordinate
                                                ClickCoordinate.click_coordinates(target_x+15,target_y,"Click")
                                            except:
                                                from droid_activities import messagebox
                                                messagebox.popup_message_box("Need to close")
                                        else:
                                            print(" NPC Msg Not Valid")
                                            from droid_activities import excelappend
                                            excelappend.append_excel('C:\\RisePT\\Daily Summary Folder'+'\\'+'RisePT_PatientCoordination_SummaryReport - '+currentdate.replace('-','.')+'.xlsx', [currentdate,TaskID,Tasktitle,Patientname,Dateofbirth,TaskAssingnee,Accountnumber,'Needs Attention','The NPC message template Are Not Valid'], 'Sheet1')
                                            continue
                                    else:
                                        print(" Already Send Msg Completed")                                 
                                    time.sleep(5)
                        #< ------ weave close ----->
                        if (TaskNumber == "1"):#( Task Title has 1 means Run the this conditions )
                            from droid_activities import windowhandle
                            switch_to_window_by_title(driver, "prompt")
                            time.sleep(5)
                            from droid_activities import ClickElement
                            ClickElement.click_element("By.XPATH", "xpath",f"(//button[.//i[contains(@class,'mdi-checkbox-marked-circle-plus-outline')]])[2]",4,"Click Task Button",driver)
                            time.sleep(5)
                            from droid_activities import ClickElement
                            #ClickElement.click_element("By.XPATH", "xpath",f"//button[.//i[normalize-space()='close']]",4,"Click Close Button",driver)
                            time.sleep(3)
                            from droid_activities import windowhandle
                            #switch_to_window_by_title(driver, "prompt")
                            time.sleep(5)
                            from datetime import datetime, timedelta
                            def add_business_days(start_date, days=2):
                                current = start_date
                                added = 0
                                while added < days:
                                    current += timedelta(days=1)
                                    if current.weekday() < 5:  # Monday=0 … Friday=4
                                        added += 1
                                return current
                            today = datetime.today()
                            Upcoming_Date = add_business_days(today)
                            Upcoming_Date=Upcoming_Date.strftime("%m/%d/%Y")
                            print(Upcoming_Date)
                            from droid_activities import ClickElement
                            #ClickElement.click_element("By.XPATH", "xpath",f"(//button[.//i[contains(@class,'mdi-checkbox-marked-circle-plus-outline')]])[2]",4,"Click Task Button",driver)
                            try:
                                from droid_activities import ClickElement
                                try:
                                    ClickElement.click_element("By.XPATH", "xpath",f"//div[normalize-space()='{Tasktitle}'] /ancestor::div[contains(@class,'ticketModalRow')] //i[contains(@class,'mdi-pencil-outline')]/ancestor::button",4,"Click Edit Button",driver)
                                except:
                                    ClickElement.click_element("By.XPATH", "xpath",f"//div[contains(normalize-space(),'Schedule Eval')]/ancestor::div[contains(@class,'ticketModalRow')]//button[.//i[contains(@class,'mdi-pencil-outline')]]",4,"Click Edit Button",driver)
                            except:
                                from droid_activities import excelappend
                                excelappend.append_excel('C:\\RisePT\\Daily Summary Folder'+'\\'+'RisePT_PatientCoordination_SummaryReport - '+currentdate.replace('-','.')+'.xlsx', [currentdate,TaskID,Tasktitle,Patientname,"N/A",TaskAssingnee,Accountnumber,'Needs Attention','1st schedule eval Edit Issue'], 'Sheet1')
                                continue
                            from droid_activities import ClickElement
                            ClickElement.click_element("By.XPATH", "xpath",f"//input[@placeholder='Add title']",4,"Click Add title",driver)
                            from droid_activities import emptyelement
                            emptyelement.type_element("By.XPATH","xpath",f"//input[@placeholder='Add title']",1,driver,"Add title Empty")
                            from droid_activities import TypeElement
                            TypeElement.type_element("By.XPATH", "xpath",f"//input[@placeholder='Add title']","2 Schedule Eval:",1,driver,"Type Quote Patient")
                            from droid_activities import ClickElement
                            ClickElement.click_element("By.XPATH", "xpath",f"//div[contains(@class,'q-field__control-container') and .//div[normalize-space(text())='Due Date']]//input",4,"Click Due Date",driver)
                            from droid_activities import ClickElement
                            ClickElement.click_element("By.XPATH", "xpath",f"//div[contains(@class,'q-field__control-container') and .//div[normalize-space(text())='Due Date']]//input",4,"Click Due Date",driver)
                            from droid_activities import emptyelement
                            emptyelement.type_element("By.XPATH","xpath",f"//div[contains(@class,'q-field__control-container') and .//div[normalize-space(text())='Due Date']]//input",1,driver,"Due Date")
                            import keyboard;keyboard.press_and_release('enter')
                            from droid_activities import TypeElement
                            TypeElement.type_element("By.XPATH", "xpath",f"//input[@aria-label='Due Date' and @placeholder='Select date']",Upcoming_Date,1,driver,"Due Date")
                            from droid_activities import ClickElement
                            ClickElement.click_element("By.XPATH", "xpath",f"//div[@role='radio' and @aria-label='High']",4,"Click High",driver) #Manual
                            from droid_activities import ClickElement
                            ClickElement.click_element("By.XPATH", "xpath",f"//button[.//div[normalize-space(.)='Save Task']]",4,"Click Save Task",driver)
                            time.sleep(3)
                            try:
                                from droid_activities import ClickElement
                                ClickElement.click_element("By.XPATH", "xpath",f"//button[contains(@class,'text-p-gray400')]//i[normalize-space(.)='close']/ancestor::button",5,"Click Save Task",driver)
                            except:
                                try:
                                    from droid_activities import ClickElement
                                    ClickElement.click_element("By.XPATH", "xpath",f"//button[contains(@class,'text-p-gray400')]//i[normalize-space(.)='close']/ancestor::button",5,"Click Save Task",driver)
                                except:
                                    print("Close Button Not Working")
                            time.sleep(3)
                            from droid_activities import excelappend
                            excelappend.append_excel('C:\\RisePT\\Daily Summary Folder'+'\\'+'RisePT_PatientCoordination_SummaryReport - '+currentdate.replace('-','.')+'.xlsx', [currentdate,TaskID,Tasktitle,Patientname,Dateofbirth,TaskAssingnee,Accountnumber,'Success','The patients workflow has been successfully processed'], 'Sheet1')
                        elif(TaskNumber == "2"): # (Task Title has 2 means activate this condition)
                            print("Solumn Part")
                            from droid_activities import openbrowser
                            from droid_activities import windowhandle
                            windowhandle.window_handle(driver,2)
                            time.sleep(4)
                            from droid_activities import CitrixImageExist
                            Solum404_Exists = CitrixImageExist.citrix_image_exist(r"C:\RisePT\Image Folder\Solumn_404.png",10, 0.8)
                            if(Solum404_Exists):
                                print(" Solum portal server Down")
                                from droid_activities import date_time
                                currentdate = date_time.date_time('%m-%d-%Y', 'current',0, "currentdate","currentdate")
                                from droid_activities import send_mail
                                tomail = ["Manikandan.c@droidal.com"]
                                ccmail = ["Manikandan.c@droidal.com"]
                                send_mail.send_email('C:\\RisePT\\Daily Summary Folder'+'\\'+'RisePT_PatientCoordination_SummaryReport - '+currentdate.replace('-','.')+'.xlsx','risept@droidal.ai','kqf8vZzhkAPeiuvp8Y',tomail,ccmail," Solum page server down issue ",'', "Solumn page Exception", 'smtp.office365.com', 587)
                                print(" Server Down")
                            time.sleep(5)
                            ClickElement.click_element("By.XPATH", "xpath",f"//a[@data-sidebar='menu-button']//span[normalize-space()='Patients']",15," Click Patients",driver)
                            time.sleep(5)
                            parts = Patientname.split()
                            first_name = parts[0]
                            last_name = parts[-1]
                            from droid_activities import ClickElement
                            ClickElement.click_element("By.XPATH", "xpath",f"//button[@aria-haspopup='menu' and normalize-space()='Actions']",1,"Add Patient",driver)
                            from droid_activities import ClickElement
                            ClickElement.click_element("By.XPATH", "xpath",f"//div[@role='menuitem' and normalize-space()='Add Patient']",1,"Add Patient",driver)
                            from droid_activities import ClickElement
                            ClickElement.click_element("By.XPATH", "xpath",f"//div[@role='menuitem' and normalize-space(text())='Manual Entry']",1,"Manual Entry",driver)
                            from droid_activities import TypeElement
                            TypeElement.type_element("By.XPATH", "xpath",f"//input[@name='firstName']",first_name,1,driver,"First Name")
                            time.sleep(1)
                            from droid_activities import TypeElement
                            TypeElement.type_element("By.XPATH", "xpath",f"//input[@name='lastName']",last_name,1,driver,"Last Name")
                            time.sleep(1)
                            print(Mobileno)
                            from droid_activities import TypeElement
                            TypeElement.type_element("By.XPATH", "xpath",f"//input[@name='phoneNumber']",f"{Mobileno}",1,driver,"Phone Number")
                            time.sleep(3)
                            # from droid_activities import hoverElement
                            # hoverElement.hover_element("By.XPATH", "xpath",f"//label[normalize-space()='Workflow Stage']",1,"workflowStageId Field",driver)
                            # time.sleep(2)
                            # ClickElement.click_element("By.XPATH", "xpath",f"//select/option[@selected and normalize-space()='3rd Attempt Call']",1," Click 3rd Attempt Call",driver)
                            time.sleep(2)
                            from selenium.webdriver.common.by import By
                            from selenium.webdriver.support.ui import WebDriverWait
                            from selenium.webdriver.support import expected_conditions as EC
                            def select_workflow_stage(option_text, driver):
                                wait = WebDriverWait(driver, 10)
                                wait.until(EC.element_to_be_clickable((By.XPATH,
                                    "//label[normalize-space()='Workflow Stage']/following-sibling::button[@role='combobox']"))).click()
                                wait.until(EC.element_to_be_clickable((By.XPATH,
                                    f"//div[@role='option' and contains(normalize-space(),'{option_text}')]"))).click()
                            select_workflow_stage("3rd Attempt Call", driver)
                            from droid_activities import hoverElement
                            hoverElement.hover_element("By.XPATH", "xpath",f"//button[normalize-space()='Create Patient']",1,"Hover create patient",driver)
                            ClickElement.click_element("By.XPATH", "xpath",f"//button[normalize-space()='Create Patient']",3," Click Create Patient",driver)
                            IS_PatientAlreadyExists = False
                            from droid_activities import ElementWait
                            Patients_Alreadyexist = ElementWait.element_wait(driver, "By.XPATH", f"//h2[text()='Patient Already Exists']/ancestor::div[contains(@class,'flex')]",10)
                            try:
                                if(Patients_Alreadyexist):
                                    from droid_activities import date_time
                                    currentdate = date_time.date_time('%m-%d-%Y', 'current',0, "currentdate","currentdate")
                                    from droid_activities import send_mail
                                    tomail = ["Manikandan.c@droidal.com"]
                                    ccmail = ["Manikandan.c@droidal.com"]
                                    send_mail.send_email('C:\\RisePT\\Daily Summary Folder'+'\\'+'RisePT_PatientCoordination_SummaryReport - '+currentdate.replace('-','.')+'.xlsx','risept@droidal.ai','kqf8vZzhkAPeiuvp8Y',tomail,ccmail," Patients already exists task= 2 ",'', " Patients already exists task= 2", 'smtp.office365.com', 587)
                                    print(" Patients already exists")
                                    ClickElement.click_element("By.XPATH", "xpath",f"//div[@role='dialog']//a[contains(@href,'/patients/')]",5," Click Link",driver)
                                    time.sleep(5)
                                    windowhandle.window_handle(driver,3)
                                    time.sleep(10)
                                    # ClickElement.click_element("By.XPATH", "xpath",f"//button[.//*[name()='svg' and contains(@class,'lucide-pencil')]][1]",5," Click Edit Button",driver)
                                    time.sleep(3)
                                    from droid_activities import hoverElement
                                    hoverElement.hover_element("By.XPATH", "xpath",f"//*[@aria-label and contains(@aria-label, 'Workflow Stage')]",1,"Hover Workflow Stage",driver)
                                    ClickElement.click_element("By.XPATH", "xpath",f"//*[@aria-label and contains(@aria-label, 'Workflow Stage')]",5," Click Workflow Stage",driver)
                                    time.sleep(1)
                                    ClickElement.click_element("By.XPATH", "xpath",f"//*[@data-value='3rd Attempt Call']",5," Click 3rd Attempt Call",driver)
                                    time.sleep(3)
                                    # ClickElement.click_element("By.XPATH", "xpath",f"//button[normalize-space()='Save']",5," Click Save",driver)
                                    time.sleep(3)
                                    windowhandle.window_handle(driver,3)
                                    driver.close()
                                    time.sleep(5)
                                    windowhandle.window_handle(driver,2)
                                    time.sleep(3)
                                    ClickElement.click_element("By.XPATH", "xpath",f"//div[@role='dialog']//button[.//span[text()='Close']]",15," Click Close",driver)
                            except:
                                print("stop")
                            time.sleep(5)
                            try:
                                windowhandle.window_handle(driver,2)
                            except:
                                print(" Window exception")
                            # ClickElement.click_element("By.XPATH", "xpath",f"//div[@role='dialog']//button[.//span[text()='Close']]",15," Click Close",driver)
                            time.sleep(5)
                            ClickElement.click_element("By.XPATH", "xpath",f"//a[@data-sidebar='menu-button']//span[normalize-space()='Patients']",15," Click Patients",driver)
                            time.sleep(3)
                            switch_to_window_by_title(driver, "prompt")
                            time.sleep(3)
                            from droid_activities import ClickElement
                            ClickElement.click_element("By.XPATH", "xpath",f"(//button[.//i[contains(@class,'mdi-checkbox-marked-circle-plus-outline')]])[2]",4,"Click Task Button",driver)
                            time.sleep(5)
                            try:
                                try:
                                    ClickElement.click_element("By.XPATH", "xpath",f"//div[normalize-space()='{Tasktitle}'] /ancestor::div[contains(@class,'ticketModalRow')] //div[normalize-space()='Mark Complete']/ancestor::button",5," Click Mark Complete",driver)
                                except:
                                    ClickElement.click_element("By.XPATH", "xpath",f"//div[contains(normalize-space(),'Schedule Eval')]/ancestor::div[contains(@class,'ticketModalRow')]//button[.//i[contains(@class,'mdi-pencil-outline')]]",5," Click Mark Complete",driver)
                            except:
                                from droid_activities import excelappend
                                excelappend.append_excel('C:\\RisePT\\Daily Summary Folder'+'\\'+'RisePT_PatientCoordination_SummaryReport - '+currentdate.replace('-','.')+'.xlsx', [currentdate,TaskID,Tasktitle,Patientname,"N/A",TaskAssingnee,Accountnumber,'Needs Attention','2nd schedule eval Edit Issue'], 'Sheet1')
                                continue
                            import time
                            time.sleep(3)
                            from droid_activities import ClickElement
                            ClickElement.click_element("By.XPATH", "xpath",f"//button[contains(@class,'text-p-gray400')]//i[normalize-space(.)='close']/ancestor::button",5,"Click Save Task",driver)
                            if(IS_PatientAlreadyExists == False):
                                from droid_activities import excelappend
                                excelappend.append_excel('C:\\RisePT\\Daily Summary Folder'+'\\'+'RisePT_PatientCoordination_SummaryReport - '+currentdate.replace('-','.')+'.xlsx', [currentdate,TaskID,Tasktitle,Patientname,Dateofbirth,TaskAssingnee,Accountnumber,'Success','The patients workflow has been successfully processed'], 'Sheet1')
                            from droid_activities import messagebox
                            #messagebox.popup_message_box('Complete the task 2 Process')
                        elif (TaskNumber == "3"):#( Task Title has 1 means Run the this conditions )
                            from droid_activities import windowhandle
                            switch_to_window_by_title(driver, "prompt")
                            time.sleep(5)
                            from droid_activities import ClickElement
                            ClickElement.click_element("By.XPATH", "xpath",f"(//button[.//i[contains(@class,'mdi-checkbox-marked-circle-plus-outline')]])[2]",4,"Click Task Button",driver)
                            time.sleep(3)
                            from droid_activities import windowhandle
                            #switch_to_window_by_title(driver, "prompt")
                            time.sleep(5)
                            from datetime import datetime, timedelta
                            def add_business_days(start_date, days=3):
                                current = start_date
                                added = 0
                                while added < days:
                                    current += timedelta(days=1)
                                    if current.weekday() < 5:  # Monday=0 … Friday=4
                                        added += 1
                                return current
                            today = datetime.today()
                            Upcoming_Date = add_business_days(today)
                            Upcoming_Date=Upcoming_Date.strftime("%m/%d/%Y")
                            print(Upcoming_Date)
                            from droid_activities import ClickElement
                            #ClickElement.click_element("By.XPATH", "xpath",f"(//button[.//i[contains(@class,'mdi-checkbox-marked-circle-plus-outline')]])[2]",4,"Click Task Button",driver)
                            try:
                                from droid_activities import ClickElement
                                try:
                                    ClickElement.click_element("By.XPATH", "xpath",f"//div[normalize-space()='{Tasktitle}'] /ancestor::div[contains(@class,'ticketModalRow')] //i[contains(@class,'mdi-pencil-outline')]/ancestor::button",4,"Click Edit Button",driver)
                                except:
                                    ClickElement.click_element("By.XPATH", "xpath",f"//div[contains(normalize-space(),'Schedule Eval')]/ancestor::div[contains(@class,'ticketModalRow')]//button[.//i[contains(@class,'mdi-pencil-outline')]]",4,"Click Edit Button",driver)
                            except:
                                from droid_activities import excelappend
                                excelappend.append_excel('C:\\RisePT\\Daily Summary Folder'+'\\'+'RisePT_PatientCoordination_SummaryReport - '+currentdate.replace('-','.')+'.xlsx', [currentdate,TaskID,Tasktitle,Patientname,"N/A",TaskAssingnee,Accountnumber,'Needs Attention','3rd schedule eval Edit Issue'], 'Sheet1')
                                continue
                            from droid_activities import ClickElement
                            ClickElement.click_element("By.XPATH", "xpath",f"//input[@placeholder='Add title']",4,"Click Add title",driver)
                            from droid_activities import emptyelement
                            emptyelement.type_element("By.XPATH","xpath",f"//input[@placeholder='Add title']",1,driver,"Add title Empty")
                            from droid_activities import TypeElement
                            TypeElement.type_element("By.XPATH", "xpath",f"//input[@placeholder='Add title']","4 Schedule Eval:",1,driver,"Type 4 Schedule Eval")
                            from droid_activities import ClickElement
                            ClickElement.click_element("By.XPATH", "xpath",f"//div[contains(@class,'q-field__control-container') and .//div[normalize-space(text())='Due Date']]//input",4,"Click Due Date",driver)
                            from droid_activities import ClickElement
                            ClickElement.click_element("By.XPATH", "xpath",f"//div[contains(@class,'q-field__control-container') and .//div[normalize-space(text())='Due Date']]//input",4,"Click Due Date",driver)
                            from droid_activities import emptyelement
                            emptyelement.type_element("By.XPATH","xpath",f"//div[contains(@class,'q-field__control-container') and .//div[normalize-space(text())='Due Date']]//input",1,driver,"Due Date")
                            import keyboard;keyboard.press_and_release('enter')
                            from droid_activities import TypeElement
                            TypeElement.type_element("By.XPATH", "xpath",f"//input[@aria-label='Due Date' and @placeholder='Select date']",Upcoming_Date,1,driver,"Due Date")
                            from droid_activities import ClickElement
                            ClickElement.click_element("By.XPATH", "xpath",f"//div[contains(@class,'text-p-subtitle1') and contains(text(),'Task Editor')]",4,"Click Task Editor",driver)
                            from droid_activities import ClickElement
                            ClickElement.click_element("By.XPATH", "xpath",f"//div[@role='radio' and @aria-label='Med']",4,"Click Med",driver) #Manual
                            from droid_activities import ClickElement
                            ClickElement.click_element("By.XPATH", "xpath",f"//button[.//div[normalize-space(.)='Save Task']]",4,"Click Save Task",driver)
                            time.sleep(3)
                            try:
                                from droid_activities import ClickElement
                                ClickElement.click_element("By.XPATH", "xpath",f"//button[contains(@class,'text-p-gray400')]//i[normalize-space(.)='close']/ancestor::button",5,"Click Save Task",driver)
                            except:
                                try:
                                    from droid_activities import ClickElement
                                    ClickElement.click_element("By.XPATH", "xpath",f"//button[contains(@class,'text-p-gray400')]//i[normalize-space(.)='close']/ancestor::button",5,"Click Save Task",driver)
                                except:
                                    print("Close Button Not Working")
                            time.sleep(3)
                            from droid_activities import excelappend
                            excelappend.append_excel('C:\\RisePT\\Daily Summary Folder'+'\\'+'RisePT_PatientCoordination_SummaryReport - '+currentdate.replace('-','.')+'.xlsx', [currentdate,TaskID,Tasktitle,Patientname,Dateofbirth,TaskAssingnee,Accountnumber,'Success','The patients workflow has been successfully processed'], 'Sheet1')
                        elif (TaskNumber == "4"):#( Task Title has 1 means Run the this conditions )
                            from droid_activities import windowhandle
                            switch_to_window_by_title(driver, "prompt")
                            time.sleep(5)
                            from droid_activities import ClickElement
                            ClickElement.click_element("By.XPATH", "xpath",f"(//button[.//i[contains(@class,'mdi-checkbox-marked-circle-plus-outline')]])[2]",4,"Click Task Button",driver)
                            time.sleep(5)
                            from datetime import datetime, timedelta
                            import calendar
                            def add_one_month_adjust_weekend(start_date):
                                year = start_date.year
                                month = start_date.month + 1
                                if month > 12:
                                    month = 1
                                    year += 1
                                last_day = calendar.monthrange(year, month)[1]
                                day = min(start_date.day, last_day)
                                result_date = datetime(year, month, day)
                                if result_date.weekday() == 5:
                                    result_date += timedelta(days=2)
                                elif result_date.weekday() == 6:
                                    result_date += timedelta(days=1)
                                return result_date
                            today = datetime.today()
                            Upcoming_Date = add_one_month_adjust_weekend(today)
                            Upcoming_Date = Upcoming_Date.strftime("%m/%d/%Y")
                            print(Upcoming_Date)
                            try:
                                from droid_activities import ClickElement
                                try:
                                    ClickElement.click_element("By.XPATH", "xpath",f"//div[normalize-space()='{Tasktitle}'] /ancestor::div[contains(@class,'ticketModalRow')] //i[contains(@class,'mdi-pencil-outline')]/ancestor::button",4,"Click Edit Button",driver)
                                except:
                                    ClickElement.click_element("By.XPATH", "xpath",f"//div[contains(normalize-space(),'Schedule Eval')]/ancestor::div[contains(@class,'ticketModalRow')]//button[.//i[contains(@class,'mdi-pencil-outline')]]",4,"Click Edit Button",driver)
                            except:
                                from droid_activities import excelappend
                                excelappend.append_excel('C:\\RisePT\\Daily Summary Folder'+'\\'+'RisePT_PatientCoordination_SummaryReport - '+currentdate.replace('-','.')+'.xlsx', [currentdate,TaskID,Tasktitle,Patientname,"N/A",TaskAssingnee,Accountnumber,'Needs Attention','4th schedule eval Edit Issue'], 'Sheet1')
                                continue
                            from droid_activities import ClickElement
                            ClickElement.click_element("By.XPATH", "xpath",f"//input[@placeholder='Add title']",4,"Click Add title",driver)
                            from droid_activities import emptyelement
                            emptyelement.type_element("By.XPATH","xpath",f"//input[@placeholder='Add title']",1,driver,"Add title Empty")
                            from droid_activities import TypeElement
                            TypeElement.type_element("By.XPATH", "xpath",f"//input[@placeholder='Add title']","Discharge",1,driver,"Type Discharge")
                            from droid_activities import ClickElement
                            ClickElement.click_element("By.XPATH", "xpath",f"//div[contains(@class,'q-field__control-container') and .//div[normalize-space(text())='Due Date']]//input",4,"Click Due Date",driver)
                            from droid_activities import ClickElement
                            ClickElement.click_element("By.XPATH", "xpath",f"//div[contains(@class,'q-field__control-container') and .//div[normalize-space(text())='Due Date']]//input",4,"Click Due Date",driver)
                            from droid_activities import emptyelement
                            emptyelement.type_element("By.XPATH","xpath",f"//div[contains(@class,'q-field__control-container') and .//div[normalize-space(text())='Due Date']]//input",1,driver,"Due Date")
                            import keyboard;keyboard.press_and_release('enter')
                            from droid_activities import TypeElement
                            TypeElement.type_element("By.XPATH", "xpath",f"//input[@aria-label='Due Date' and @placeholder='Select date']",Upcoming_Date,1,driver,"Due Date")
                            from droid_activities import ClickElement
                            ClickElement.click_element("By.XPATH", "xpath",f"//div[contains(@class,'text-p-subtitle1') and contains(text(),'Task Editor')]",4,"Click Task Editor",driver)
                            from droid_activities import ClickElement
                            ClickElement.click_element("By.XPATH", "xpath",f"//div[@role='radio' and @aria-label='Low']",4,"Click Low",driver) #Manual
                            from droid_activities import ClickElement
                            ClickElement.click_element("By.XPATH", "xpath",f"//button[.//div[normalize-space(.)='Save Task']]",4,"Click Save Task",driver)
                            time.sleep(3)
                            try:
                                from droid_activities import ClickElement
                                ClickElement.click_element("By.XPATH", "xpath",f"//button[contains(@class,'text-p-gray400')]//i[normalize-space(.)='close']/ancestor::button",5,"Click Save Task",driver)
                            except:
                                try:
                                    from droid_activities import ClickElement
                                    ClickElement.click_element("By.XPATH", "xpath",f"//button[contains(@class,'text-p-gray400')]//i[normalize-space(.)='close']/ancestor::button",5,"Click Save Task",driver)
                                except:
                                    print("Close Button Not Working")
                            time.sleep(3)
                            from droid_activities import excelappend
                            excelappend.append_excel('C:\\RisePT\\Daily Summary Folder'+'\\'+'RisePT_PatientCoordination_SummaryReport - '+currentdate.replace('-','.')+'.xlsx', [currentdate,TaskID,Tasktitle,Patientname,Dateofbirth,TaskAssingnee,Accountnumber,'Success','The patients workflow has been successfully processed'], 'Sheet1')    
                    except Exception as Er:
                        print("Reporting Task Patients part issue")
                        import traceback
                        Er = traceback.format_exc()
                        print(f"An error occurred: {Er}")
                        from droid_activities import excelappend
                        excelappend.append_excel('C:\\RisePT\\Daily Summary Folder'+'\\'+'RisePT_PatientCoordination_SummaryReport - '+currentdate.replace('-','.')+'.xlsx', [currentdate,TaskID,Tasktitle,Patientname,"N/A",TaskAssingnee,Accountnumber,'Needs Attention','This patient needs attention for further review'], 'Sheet1')
                        switch_to_window_by_title(driver, "prompt")
                        is_Exception = True                      
                from droid_activities import date_time
                currentdate = date_time.date_time('%m-%d-%Y', 'current',0, "currentdate","currentdate")
                from droid_activities import send_mail
                tomail = ["Manikandan.c@droidal.com"]
                ccmail = ["Manikandan.c@droidal.com"]
                send_mail.send_email('C:\\RisePT\\Daily Summary Folder'+'\\'+'RisePT_PatientCoordination_SummaryReport - '+currentdate.replace('-','.')+'.xlsx','risept@droidal.ai','kqf8vZzhkAPeiuvp8Y',tomail,ccmail," Text Task are completed ",'', "summaryfile", 'smtp.office365.com', 587)
                
                #<---------------- 3 rd Attempt Call -------------------------->
                try:   
                    time.sleep(5)
                    windowhandle.window_handle(driver,2)
                    from droid_activities import date_time
                    currentdate = date_time.date_time('%m-%d-%Y', 'current',0, "currentdate","currentdate")
                    from droid_activities import FileExists
                    from droid_activities import hoverElement
                    hoverElement.hover_element("By.XPATH", "xpath",f"//div[contains(@class, 'inline-flex')]/h2[contains(text(), '3rd Attempt Call')]",1,"3rd Attempt Call",driver)
                    time.sleep(1)
                    from droid_activities import ClickElement
                    ClickElement.click_element("By.XPATH", "xpath",f"//div[contains(@class, 'inline-flex')]/h2[contains(text(), '3rd Attempt Call')]",1," Click 3rd Attempt Call",driver)
                    time.sleep(1)
                    try:
                        from droid_activities import GetTextElement
                        Follow_Upscount = GetTextElement.get_textElement("By.XPATH",f"//div[@class='flex items-center justify-between mb-4'] [.//h2[normalize-space(text())='3rd Attempt Call']] /div[contains(@class,'inline-flex') and contains(@class,'font-semibold')]",1,"Get 3rd Attempt Call Count",driver)
                    except:
                        Follow_Upscount="0"
                    phone_numbers = []
                    Follow_Upscount=int(Follow_Upscount)
                    print(Follow_Upscount)
                    Loop_Count=1
                    Increment_number=1
                    while(True):
                        if(Follow_Upscount>=Loop_Count):
                            from droid_activities import ClickElement
                            time.sleep(3)
                            while(True):
                                try:
                                    from droid_activities import hoverElement
                                    hoverElement.hover_element("By.XPATH", "xpath",f"(//h2[normalize-space()='3rd Attempt Call']  /following::div[@role='button' and @aria-roledescription='draggable'])[{Increment_number}]",1,"3rd Attempt Call",driver)
                                    time.sleep(1)
                                    ClickElement.click_element("By.XPATH", "xpath",f"(//h2[normalize-space()='3rd Attempt Call']  /following::div[@role='button' and @aria-roledescription='draggable'])[{Increment_number}]",5," Click 3rd Attempt Call Patients",driver)
                                    break
                                except:
                                    print("click extra patinents")
                                    from droid_activities import hoverElement
                                    hoverElement.hover_element("By.XPATH", "xpath",f"//h2[text()='3rd Attempt Call']/ancestor::div[contains(@class, 'flex items-center')]//following-sibling::div//button[contains(text(), 'Load More')]",1,"Load more for 3rd Attempt Call",driver)
                                    time.sleep(1)
                                    ClickElement.click_element("By.XPATH", "xpath",f"//h2[text()='3rd Attempt Call']/ancestor::div[contains(@class, 'flex items-center')]//following-sibling::div//button[contains(text(), 'Load More')]",5," Click Load More Button",driver)# need to add click extra patient step
                                    time.sleep(2)
                            while(True):
                                from droid_activities import ElementWait
                                PatientDetails_exist = ElementWait.element_wait(driver, "By.XPATH", f"//button[@role='tab' and normalize-space()='Patient Details']",10)
                                if(PatientDetails_exist == True):
                                    break
                                else:
                                    time.sleep(5)
                            from droid_activities import GetTextElement
                            Third_Patient_PNO = GetTextElement.get_textElement("By.XPATH",f"//div[contains(@aria-label, 'Phone Number')]",1,"Get Phone Numner",driver)
                            if (Loop_Count >= 2):
                                if Third_Patient_PNO in phone_numbers:
                                    Increment_number = Increment_number+1
                                    ClickElement.click_element("By.XPATH", "xpath",f"//button[.//span[normalize-space(.)='Close']]",1," Click Close",driver)
                                    continue
                            phone_numbers.append(Third_Patient_PNO)
                            print(Third_Patient_PNO)
                            from droid_activities import ElementWait
                            PatientDetails_exist = ElementWait.element_wait(driver, "By.XPATH", f"//button[@role='tab' and normalize-space()='Patient Details']",10)
                            launchcount = int(0) #int
                            if PatientDetails_exist == True: #range
                                from droid_activities import message_box_delay
                                message_box_delay.show_timed_message_box('Launch Page Exist - PatientHeader', 1)
                                ClickElement.click_element("By.XPATH", "xpath",f"//button[@role='tab' and contains(normalize-space(.), 'Patient Details')]",1," Click Patient Details",driver)
                                from droid_activities import GetTextElement
                                ThirdFname = GetTextElement.get_textElement("By.XPATH",f"//div[@role='button'][contains(@aria-label, 'First Name')]",1,"First Name",driver)
                                print(ThirdFname)
                                from droid_activities import GetTextElement
                                ThirdLname = GetTextElement.get_textElement("By.XPATH",f"//div[@role='button'][contains(@aria-label, 'Last Name')]",1,"Last Name",driver)
                                print(ThirdLname)
                                from droid_activities import GetTextElement
                                Third_DOB = GetTextElement.get_textElement("By.XPATH",f"//div[@role='button'][contains(@aria-label, 'Date of Birth')]",1,"Get DOB",driver)
                                print(Third_DOB)
                                from droid_activities import GetTextElement
                                Get_FUComments = GetTextElement.get_textElement("By.XPATH",f"//*[@role='button' and contains(@aria-label,'Comments')]",1,"Get OAR Comments",driver)
                                time.sleep(1)
                                from droid_activities import GetTextElement
                                Get_Tag = GetTextElement.get_textElement("By.XPATH",f"//*[@role='button' and contains(@aria-label,'Tags')]",1,"Get Tag",driver)
                                print(Get_Tag)
                                if(Get_Tag == "Active Campaign"):
                                    ActiveCampaine = True
                                    print(" Active Compaine Are Available")
                                else:
                                    ActiveCampaine = False
                                    print("Active compaine not commimg")
                                from droid_activities import ClickElement
                                from selenium.webdriver.common.by import By
                                from selenium.webdriver.support.ui import WebDriverWait
                                from selenium.webdriver.support import expected_conditions as EC
                                from datetime import datetime
                                # ---------- FIRST OUTGOING CALL ----------
                                try:
                                    from droid_activities import ElementWait
                                    Firstoutgoingcall_exist = ElementWait.element_wait(driver, "By.XPATH", f"(//div[.//div[normalize-space()='Outgoing Call']]//div[@data-date])[1]",10)
                                    xpath1 = "(//div[.//div[normalize-space()='Outgoing Call']]//div[@data-date])[1]"
                                    elem1 = driver.find_element(By.XPATH, xpath1)    
                                    date_text_1 = elem1.get_attribute("data-date")  # best option
                                    print(date_text_1)
                                    OutDate_1 = datetime.strptime(date_text_1, "%A, %B %d")   
                                except Exception as e:
                                    print(f"An error occurred while reading the Excel file: {e}")
                                    date_text_1 = "Thursday, November 13"
                                    OutDate_1 = datetime.strptime(date_text_1, "%A, %B %d")
                                # ---------- SECOND OUTGOING CALL ----------
                                try:
                                    from droid_activities import ElementWait
                                    Task_exist = ElementWait.element_wait(driver, "By.XPATH", f"//div[contains(@class,'font-medium') and contains(@class,'text-gray-900') and text()='Task']/ancestor::div[contains(@class,'bg-purple-50')]",10)
                                    xpath2 = "(//div[.//div[normalize-space()='Outgoing Call']]//div[@data-date])[2]"
                                    elem2 = driver.find_element(By.XPATH, xpath2)    
                                    date_text_2 = elem2.get_attribute("data-date")
                                    print(date_text_2)
                                    OutDate_2 = datetime.strptime(date_text_2, "%A, %B %d")
                                except Exception as e:
                                    Task_exist=False
                                    print(f"An error occurred while reading the Excel file: {e}")
                                    print("Second Outgoing call not available")
                                    date_text_2 = "Tuesday, November 25"
                                    OutDate_2 = datetime.strptime(date_text_2, "%A, %B %d")
                                difference = abs((OutDate_2 - OutDate_1).days)
                                # if (Firstoutgoingcall_exist == True):
                                if (Firstoutgoingcall_exist == True or Task_exist == True):
                                    time.sleep(1)
                                    from droid_activities import windowhandle
                                    switch_to_window_by_title(driver, "prompt")
                                    time.sleep(3)
                                    from droid_activities import ClickElement
                                    ClickElement.click_element("By.XPATH", "xpath",f"//a[.//div[normalize-space()='Patients']]",1,"Patients Menu",driver)
                                    from droid_activities import hoverElement
                                    hoverElement.hover_element("By.XPATH", "xpath",f"//input[@*='Search patients'][@type='search']",1,"Patient Name Text Field",driver)
                                    time.sleep(1)
                                    from droid_activities import ClickElement
                                    ClickElement.click_element("By.XPATH", "xpath",f"//input[@*='Search patients'][@type='search']",1,"patient Name text field",driver)
                                    from droid_activities import emptyelement
                                    emptyelement.type_element("By.XPATH","xpath",f"//input[@*='Search patients'][@type='search']",1,driver,"Patient Name Text Field")
                                    import time
                                    time.sleep(1)
                                    from droid_activities import TypeElement
                                    TypeElement.type_element("By.XPATH", "xpath",f"//input[@*='Search patients'][@type='search']",Third_Patient_PNO,1,driver,"Type Patient Phone Number")
                                    import time
                                    time.sleep(1)
                                    from droid_activities import ElementWait
                                    Patient_notexist = ElementWait.element_wait(driver, "By.XPATH", f"//div[contains(@class,'text-p-gray600')]//div[contains(.,'No results, try searching')]",10)
                                    if(Patient_notexist == True):
                                        from droid_activities import ClickElement
                                        ClickElement.click_element("By.XPATH", "xpath",f"//div[contains(@class,'p-listview')]//button[contains(@class,'outline-p-blue600')]",1,"ADD PAtients Button",driver)
                                        import time
                                        time.sleep(3)
                                        from droid_activities import ClickElement
                                        ClickElement.click_element("By.XPATH", "xpath",f"//input[@data-testid='patient-firstname']",1,"First Name field",driver)
                                        from droid_activities import TypeElement
                                        TypeElement.type_element("By.XPATH", "xpath",f"//input[@data-testid='patient-firstname']",ThirdFname,1,driver,"Type First Name")
                                        from droid_activities import ClickElement
                                        ClickElement.click_element("By.XPATH", "xpath",f"//input[@data-testid='patient-lastname']",1,"Last Name field",driver)
                                        from droid_activities import TypeElement
                                        TypeElement.type_element("By.XPATH", "xpath",f"//input[@data-testid='patient-lastname']",ThirdLname,1,driver,"Type Last Name")
                                        from droid_activities import ClickElement
                                        ClickElement.click_element("By.XPATH", "xpath",f"//input[@data-testid='patient-dateofbirth']",1,"Date of Birth field",driver)
                                        from droid_activities import TypeElement
                                        TypeElement.type_element("By.XPATH", "xpath",f"//input[@data-testid='patient-dateofbirth']",Third_DOB,1,driver,"Type Date of Birth")
                                        try:
                                            from droid_activities import ClickElement
                                            ClickElement.click_element("By.XPATH", "xpath",f"//div[@data-testid='patient-gender']",1,"Gender field",driver)
                                        except:
                                            time.sleep(5)
                                        from droid_activities import ClickElement
                                        ClickElement.click_element("By.XPATH", "xpath",f"//div[@role='option']//span[text()='Female']",1,"Click Female",driver)
                                        from droid_activities import ClickElement
                                        ClickElement.click_element("By.XPATH", "xpath",f"//input[@aria-label='Mobile Phone *']",1,"Mobile Phone field",driver)
                                        from droid_activities import TypeElement
                                        TypeElement.type_element("By.XPATH", "xpath",f"//input[@aria-label='Mobile Phone *']",Third_Patient_PNO,1,driver,"Type Mobile Phone ")
                                        from droid_activities import ClickElement
                                        ClickElement.click_element("By.XPATH", "xpath",f"//button[.//span[normalize-space()='Create Patient']]",1,"Click Create Patients",driver)
                                        time.sleep(5)
                                    try:
                                        from droid_activities import ClickElement
                                        ClickElement.click_element("By.XPATH", "xpath",f"//div[contains(@class, 'text-weight-medium') and contains(@class, 'text-subtitle1')]",1,"Patient Profile",driver)
                                    except:
                                        print(" Patients Not found")
                                    from droid_activities import hoverElement
                                    hoverElement.hover_element("By.XPATH", "xpath",f"//div[contains(@class,'q-chip')][.//div[normalize-space()='Visits']]",1,"Visits",driver)
                                    from droid_activities import ClickElement
                                    ClickElement.click_element("By.XPATH", "xpath",f"//div[contains(@class,'q-chip')][.//div[normalize-space()='Visits']]",1,"Visits Menu",driver)
                                    time.sleep(3)
                                    from datetime import datetime, timedelta
                                    def add_business_days(start_date, days=1):
                                        current = start_date
                                        added = 0
                                        while added < days:
                                            current += timedelta(days=1)
                                            if current.weekday() < 5:  # Monday=0 … Friday=4
                                                added += 1
                                        return current
                                    today = datetime.today()
                                    Upcoming_Date = add_business_days(today)
                                    Upcoming_Date=Upcoming_Date.strftime("%m/%d/%Y")
                                    print(Upcoming_Date)
                                    from droid_activities import GetTextElement 
                                    Get_future= GetTextElement.get_textElement("By.XPATH",f"//div[normalize-space(text())='Future']/following-sibling::div[normalize-space()]",1,"Get Future",driver)
                                    print(Get_future)
                                    Get_future=int(Get_future)
                                    from droid_activities import ElementWait
                                    visit_missing = ElementWait.element_wait(driver, "By.XPATH", f"//i[@class='p-pa-xs q-icon text-p-red600 mdi mdi-alert-outline']",10)
                                    Get_All= GetTextElement.get_textElement("By.XPATH",f"//button[.//div[normalize-space()='All']]//div[contains(@class,'bg-p')]",1,"Get All",driver)
                                    print(Get_All)
                                    from droid_activities import ElementWait
                                    No_Visits = ElementWait.element_wait(driver, "By.XPATH", f"//*[contains(@class,'bg-p-red50')]//*[contains(@class,'omni-type-medium')]",10)
                                    print(No_Visits)
                                    Get_All=int(Get_All)
                                    from droid_activities import GetTextElement 
                                    Get_future= GetTextElement.get_textElement("By.XPATH",f"//div[normalize-space()='Future']/following-sibling::div[1]",1,"Get Future",driver)
                                    print(Get_future)
                                    Priority = False
                                    Get_future=int(Get_future)
                                    if Get_future <= 0:
                                        from droid_activities import ClickElement
                                        ClickElement.click_element("By.XPATH", "xpath",f"(//button[.//i[contains(@class,'mdi-checkbox-marked-circle-plus-outline')]])[2]",4,"Click Task Button",driver)
                                        time.sleep(2)
                                        from droid_activities import ClickElement
                                        ClickElement.click_element("By.XPATH", "xpath",f"//button[.//div[normalize-space(text())='Add New Task']]",4,"Click Add New Button",driver)
                                        from droid_activities import ClickElement
                                        ClickElement.click_element("By.XPATH", "xpath",f"//input[@placeholder='Add title']",4,"Click Add title",driver)
                                        from droid_activities import emptyelement
                                        emptyelement.type_element("By.XPATH","xpath",f"//input[@placeholder='Add title']",1,driver,"Add title Empty")
                                        if(ActiveCampaine == True):
                                            from droid_activities import TypeElement
                                            TypeElement.type_element("By.XPATH", "xpath",f"//input[@placeholder='Add title']","1 Schedule Eval",1,driver,"Type 2 Schedule Eval Patient")
                                        elif(ActiveCampaine != True):
                                            Priority = True
                                            from droid_activities import TypeElement
                                            TypeElement.type_element("By.XPATH", "xpath",f"//input[@placeholder='Add title']","3 Schedule Eval",1,driver,"Type 2 Schedule Eval Patient")
                                            from datetime import datetime, timedelta
                                            def add_business_days(start_date, days=2):
                                                current = start_date
                                                added = 0
                                                while added < days:
                                                    current += timedelta(days=1)
                                                    if current.weekday() < 5:  # Monday=0 … Friday=4
                                                        added += 1
                                                return current
                                            today = datetime.today()
                                            Upcoming_Date = add_business_days(today)
                                            Upcoming_Date=Upcoming_Date.strftime("%m/%d/%Y")
                                            print(Upcoming_Date)
                                        from droid_activities import ClickElement
                                        ClickElement.click_element("By.XPATH", "xpath",f"//textarea[@aria-label='Description']",4,"Click Add title",driver)
                                        from droid_activities import emptyelement
                                        emptyelement.type_element("By.XPATH","xpath",f"//textarea[@aria-label='Description']",1,driver,"Add title Empty")
                                        from droid_activities import TypeElement
                                        TypeElement.type_element("By.XPATH", "xpath",f"//textarea[@aria-label='Description']",f" {Get_FUComments}",1,driver,"Type OAR Patient")
                                        from droid_activities import ClickElement
                                        ClickElement.click_element("By.XPATH", "xpath",f"//div[contains(@class,'q-field__control-container') and .//div[normalize-space(text())='Due Date']]//input",4,"Click Due Date",driver)
                                        from droid_activities import ClickElement
                                        ClickElement.click_element("By.XPATH", "xpath",f"//div[contains(@class,'q-field__control-container') and .//div[normalize-space(text())='Due Date']]//input",4,"Click Due Date",driver)
                                        from droid_activities import emptyelement
                                        emptyelement.type_element("By.XPATH","xpath",f"//div[contains(@class,'q-field__control-container') and .//div[normalize-space(text())='Due Date']]//input",1,driver,"Due Date")
                                        import keyboard;keyboard.press_and_release('enter')
                                        from droid_activities import TypeElement
                                        TypeElement.type_element("By.XPATH", "xpath",f"//input[@aria-label='Due Date' and @placeholder='Select date']",Upcoming_Date,1,driver,"Due Date")
                                        time.sleep(3)
                                        from droid_activities import ClickElement
                                        ClickElement.click_element("By.XPATH", "xpath",f"//textarea[@aria-label='Description']",4,"Click Add title",driver)
                                        if(Priority == True):
                                            from droid_activities import ClickElement
                                            ClickElement.click_element("By.XPATH", "xpath",f"//div[@role='radio' and @aria-label='Med']",4,"Click High",driver) #Manual
                                        else:
                                            from droid_activities import ClickElement
                                            ClickElement.click_element("By.XPATH", "xpath",f"//div[@role='radio' and @aria-label='High']",4,"Click High",driver)
                                        import time
                                        time.sleep(1)
                                        from droid_activities import hoverElement
                                        hoverElement.hover_element("By.XPATH", "xpath",f"//label[.//div[normalize-space(text())='Assign to someone']]",2,"Assign to someone",driver)
                                        from droid_activities import ClickElement
                                        ClickElement.click_element("By.XPATH", "xpath",f"//label[.//div[normalize-space(text())='Assign to someone']]",4,"Click Assign to someone",driver)
                                        from droid_activities import TypeElement
                                        TypeElement.type_element("By.XPATH", "xpath",f"//input[@placeholder='Search' and @type='search']","jen simpson",1,driver,"Select assignee")
                                        from droid_activities import ClickElement
                                        ClickElement.click_element("By.XPATH", "xpath",f"//div[contains(@class,'p-select__option-title') and normalize-space()='Jen Simpson']",4,"ClickJen Simpson",driver)
                                        from droid_activities import ClickElement
                                        ClickElement.click_element("By.XPATH", "xpath",f"//button[.//div[normalize-space(.)='Save Task']]",4,"Click Save Task",driver)
                                        from droid_activities import ClickElement
                                        ClickElement.click_element("By.XPATH", "xpath",f"//div[.//div[text()='Task List']]//button[.//i[text()='close']]",4,"Click Close Button",driver)
                                        time.sleep(3)
                                        from droid_activities import windowhandle
                                        windowhandle.window_handle(driver,2)
                                        from droid_activities import ClickElement
                                        ClickElement.click_element("By.XPATH", "xpath",f"(//button[@aria-haspopup='menu' and normalize-space()='Actions'])[2]",3,"Click Action",driver)
                                        ClickElement.click_element("By.XPATH", "xpath",f"//div[@role='menuitem' and contains(., 'Remove from Workflow')]",3,"Click Case not used",driver)
                                        #ClickElement.click_element("By.XPATH", "xpath",f"//button[.//span[normalize-space(.)='Close']]",1," Click Close",driver)
                                        from droid_activities import excelappend
                                        excelappend.append_excel('C:\\RisePT\\Daily Summary Folder'+'\\'+'RisePT_PatientCoordination_SummaryReport - '+currentdate.replace('-','.')+'.xlsx', [currentdate,"N/A","3rd Attempts",ThirdFname+" "+ThirdLname,Third_DOB,"N/A","N/A",'Success','This patient has been assigned a task and removed from the workflow'], 'Sheet1')
                                        Loop_Count=Loop_Count+1
                                    else: #Future Available
                                        print("Future Available")
                                        time.sleep(3)
                                        from droid_activities import windowhandle
                                        windowhandle.window_handle(driver,2)
                                        time.sleep(4)
                                        ClickElement.click_element("By.XPATH", "xpath",f"//button[@role='tab' and contains(normalize-space(.), 'Patient Details')]",1," Click Patient Details",driver)
                                        from droid_activities import ClickElement
                                        ClickElement.click_element("By.XPATH", "xpath",f"//div[contains(@aria-label,'Workflow Stage')]",1," Click Workflow Stage",driver)
                                        from droid_activities import ClickElement
                                        ClickElement.click_element("By.XPATH", "xpath",f"//div[@role='option' and normalize-space(text())='Scheduled Patients']",1," Click Scheduled Patients ",driver)
                                        ClickElement.click_element("By.XPATH", "xpath",f"//button[.//span[normalize-space(.)='Close']]",1," Click Close",driver)
                                        from droid_activities import excelappend
                                        excelappend.append_excel('C:\\RisePT\\Daily Summary Folder'+'\\'+'RisePT_PatientCoordination_SummaryReport - '+currentdate.replace('-','.')+'.xlsx', [currentdate,"N/A","3rd Attempts",ThirdFname+" "+ThirdLname,Third_DOB,"N/A","N/A",'Success','Future Visits Available to Move to Scheduled Patients'], 'Sheet1')
                                        Loop_Count=Loop_Count+1  
                                else: #no call Available
                                    import time
                                    time.sleep(3)
                                    from droid_activities import message_box_delay
                                    message_box_delay.show_timed_message_box('No Launch Page Exist -PatientHeader', 1)
                                    ClickElement.click_element("By.XPATH", "xpath",f"//button[.//span[normalize-space(.)='Close']]",1," Click Close",driver)
                                    from droid_activities import excelappend
                                    excelappend.append_excel('C:\\RisePT\\Daily Summary Folder'+'\\'+'RisePT_PatientCoordination_SummaryReport - '+currentdate.replace('-','.')+'.xlsx', [currentdate,"N/A","3rd Attempts",ThirdFname+" "+ThirdLname,Third_DOB,"N/A","N/A",'Needs Attention','Outgoing calls not available'], 'Sheet1')
                                    Loop_Count=Loop_Count+1
                            else: #Else Start - Not Valid Out Going Call 
                                import time
                                time.sleep(3)
                                from droid_activities import message_box_delay
                                message_box_delay.show_timed_message_box('No Launch Page Exist -PatientHeader', 1)
                                ClickElement.click_element("By.XPATH", "xpath",f"//button[.//span[normalize-space(.)='Close']]",1," Click Close",driver)
                                from droid_activities import excelappend
                                excelappend.append_excel('C:\\RisePT\\Daily Summary Folder'+'\\'+'RisePT_PatientCoordination_SummaryReport - '+currentdate.replace('-','.')+'.xlsx', [currentdate,"N/A","3rd Attempts",ThirdFname+" "+ThirdLname,Third_DOB,"N/A","N/A",'Needs Attention','This patient outgoing call validation has failed, so skipped this patient'], 'Sheet1')
                                Loop_Count=Loop_Count+1
                        else:
                            print(" Completed")
                            break
                    else: #else for While loop break condition for Follow Up call column
                        print("All the Valid Follow Up patients are Completed")
                        break 
                except:
                    print("Except 3rd attempt Call")
                    import traceback
                    Er = traceback.format_exc()
                    print(f"An error occurred: {Er}") 
                    time.sleep(2)  
                
                #<------------ Follow ups Parts are Process Start ---------------> 
                try:   
                    time.sleep(5)
                    windowhandle.window_handle(driver,2)
                    from droid_activities import date_time
                    currentdate = date_time.date_time('%m-%d-%Y', 'current',0, "currentdate","currentdate")
                    from droid_activities import FileExists
                    from droid_activities import hoverElement
                    hoverElement.hover_element("By.XPATH", "xpath",f"//div[contains(@class, 'inline-flex')]/h2[contains(text(), 'Follow Up Call')]",1,"Follow Up Call",driver)
                    time.sleep(1)
                    from droid_activities import ClickElement
                    ClickElement.click_element("By.XPATH", "xpath",f"//div[contains(@class, 'inline-flex')]/h2[contains(text(), 'Follow Up Call')]",1," Click Follow Up Call",driver)
                    time.sleep(1)
                    try:
                        from droid_activities import GetTextElement
                        Follow_Upscount = GetTextElement.get_textElement("By.XPATH",f"//div[@class='flex items-center justify-between mb-4'] [.//h2[normalize-space(text())='Follow Up Call']] /div[contains(@class,'inline-flex') and contains(@class,'font-semibold')]",1,"Get Follow Up Call Count",driver)
                    except:
                        Follow_Upscount="0"
                    phone_numbers = []
                    Follow_Upscount=int(Follow_Upscount)
                    print(Follow_Upscount)
                    Loop_Count=1
                    Increment_number=1
                    while(True):
                        if(Follow_Upscount>=Loop_Count):
                            from droid_activities import ClickElement
                            time.sleep(3)
                            while(True):
                                try:
                                    from droid_activities import hoverElement
                                    hoverElement.hover_element("By.XPATH", "xpath",f"(//h2[normalize-space()='Follow Up Call']  /following::div[@role='button' and @aria-roledescription='draggable'])[{Increment_number}]",1,"4th Attempt Call",driver)
                                    time.sleep(1)
                                    ClickElement.click_element("By.XPATH", "xpath",f"(//h2[normalize-space()='Follow Up Call']  /following::div[@role='button' and @aria-roledescription='draggable'])[{Increment_number}]",5," Click 4th Attempt Call Patients",driver)
                                    break
                                except:
                                    print("click extra patinents")
                                    from droid_activities import hoverElement
                                    hoverElement.hover_element("By.XPATH", "xpath",f"//h2[text()='Follow Up Call']/ancestor::div[contains(@class, 'flex items-center')]//following-sibling::div//button[contains(text(), 'Load More')]",1,"Load more for follow up call",driver)
                                    time.sleep(1)
                                    ClickElement.click_element("By.XPATH", "xpath",f"//h2[text()='Follow Up Call']/ancestor::div[contains(@class, 'flex items-center')]//following-sibling::div//button[contains(text(), 'Load More')]",5," Click Load More Button",driver)# need to add click extra patient step
                                    time.sleep(2)
                            while(True):
                                from droid_activities import ElementWait
                                PatientDetails_exist = ElementWait.element_wait(driver, "By.XPATH", f"//button[@role='tab' and normalize-space()='Patient Details']",10)
                                if(PatientDetails_exist == True):
                                    break
                                else:
                                    time.sleep(5)
                            from droid_activities import GetTextElement
                            FollowUp_Patient_PNO = GetTextElement.get_textElement("By.XPATH",f"//div[contains(@aria-label, 'Phone Number')]",1,"Get Phone Numner",driver)
                            if (Loop_Count >= 2):
                                if FollowUp_Patient_PNO in phone_numbers:
                                    Increment_number = Increment_number+1
                                    ClickElement.click_element("By.XPATH", "xpath",f"//button[.//span[normalize-space(.)='Close']]",1," Click Close",driver)
                                    continue
                            phone_numbers.append(FollowUp_Patient_PNO)
                            print(FollowUp_Patient_PNO)
                            from droid_activities import ElementWait
                            PatientDetails_exist = ElementWait.element_wait(driver, "By.XPATH", f"//button[@role='tab' and normalize-space()='Patient Details']",10)
                            launchcount = int(0) #int
                            if PatientDetails_exist == True: #range
                                from droid_activities import message_box_delay
                                message_box_delay.show_timed_message_box('Launch Page Exist - PatientHeader', 1)
                                ClickElement.click_element("By.XPATH", "xpath",f"//button[@role='tab' and contains(normalize-space(.), 'Patient Details')]",1," Click Patient Details",driver)
                                from droid_activities import GetTextElement
                                Fname = GetTextElement.get_textElement("By.XPATH",f"//div[@role='button'][contains(@aria-label, 'First Name')]",1,"First Name",driver)
                                print(Fname)
                                from droid_activities import GetTextElement
                                Lname = GetTextElement.get_textElement("By.XPATH",f"//div[@role='button'][contains(@aria-label, 'Last Name')]",1,"Last Name",driver)
                                print(Lname)
                                from droid_activities import GetTextElement
                                DOB_4th = GetTextElement.get_textElement("By.XPATH",f"//div[@role='button'][contains(@aria-label, 'Date of Birth')]",1,"Get DOB",driver)
                                print(DOB_4th)
                                from droid_activities import GetTextElement
                                Get_Tag = GetTextElement.get_textElement("By.XPATH",f"//*[@role='button' and contains(@aria-label,'Tags')]",1,"Get Tag",driver)
                                print(Get_Tag)
                                if(Get_Tag == "Active Campaign"):
                                    ActiveCampaine = True
                                    print(" Active Compaine Are Available")
                                else:
                                    ActiveCampaine = False
                                    print("Active compaine not commimg")
                                from droid_activities import GetTextElement
                                Get_FUComments = GetTextElement.get_textElement("By.XPATH",f"//*[@role='button' and contains(@aria-label,'Comments')]",1,"Get OAR Comments",driver)
                                time.sleep(1)
                                from droid_activities import ClickElement
                                from selenium.webdriver.common.by import By
                                from selenium.webdriver.support.ui import WebDriverWait
                                from selenium.webdriver.support import expected_conditions as EC
                                from datetime import datetime
                                # ---------- FIRST OUTGOING CALL ----------
                                try:
                                    from droid_activities import ElementWait
                                    Firstoutgoingcall_exist = ElementWait.element_wait(driver, "By.XPATH", f"(//div[.//div[normalize-space()='Outgoing Call']]//div[@data-date])[1]",10)
                                    xpath1 = "(//div[.//div[normalize-space()='Outgoing Call']]//div[@data-date])[1]"
                                    elem1 = driver.find_element(By.XPATH, xpath1)    
                                    date_text_1 = elem1.get_attribute("data-date")  # best option
                                    print(date_text_1)
                                    OutDate_1 = datetime.strptime(date_text_1, "%A, %B %d")   
                                except Exception as e:
                                    print(f"An error occurred while reading the Excel file: {e}")
                                    date_text_1 = "Thursday, November 13"
                                    OutDate_1 = datetime.strptime(date_text_1, "%A, %B %d")
                                # ---------- SECOND OUTGOING CALL ----------
                                try:
                                    from droid_activities import ElementWait
                                    Secondoutgoingcall_exist = ElementWait.element_wait(driver, "By.XPATH", f"(//div[.//div[normalize-space()='Outgoing Call']]//div[@data-date])[2]",10)
                                    xpath2 = "(//div[.//div[normalize-space()='Outgoing Call']]//div[@data-date])[2]"
                                    elem2 = driver.find_element(By.XPATH, xpath2)    
                                    date_text_2 = elem2.get_attribute("data-date")
                                    print(date_text_2)
                                    OutDate_2 = datetime.strptime(date_text_2, "%A, %B %d")
                                except Exception as e:
                                    Secondoutgoingcall_exist=False
                                    print(f"An error occurred while reading the Excel file: {e}")
                                    print("Second Outgoing call not available")
                                    date_text_2 = "Tuesday, November 25"
                                    OutDate_2 = datetime.strptime(date_text_2, "%A, %B %d")
                                difference = abs((OutDate_2 - OutDate_1).days)
                                if (Firstoutgoingcall_exist == True and Secondoutgoingcall_exist == True):
                                    if(ActiveCampaine != True):
                                        time.sleep(4)
                                        ClickElement.click_element("By.XPATH", "xpath",f"//button[@role='tab' and contains(normalize-space(.), 'Patient Details')]",1," Click Patient Details",driver)
                                        from droid_activities import ClickElement
                                        ClickElement.click_element("By.XPATH", "xpath",f"//div[contains(@aria-label,'Workflow Stage')]",1," Click Workflow Stage",driver)
                                        from droid_activities import ClickElement
                                        ClickElement.click_element("By.XPATH", "xpath",f"//div[@role='option' and normalize-space(text())='Lost- Discharge Patient']",1," Click Lost- Discharge Patient",driver)
                                        from datetime import datetime
                                        from dateutil.relativedelta import relativedelta
                                        Today_date = datetime.today()
                                        one_month_after = Today_date + relativedelta(months=1)
                                        Onemonth_date = one_month_after.strftime("%m/%d/%Y")
                                        from droid_activities import ClickElement
                                        ClickElement.click_element("By.XPATH", "xpath",f"//div[starts-with(@aria-label, 'Comments,')]",1," Click Lost- Discharge Patient",driver)
                                        from droid_activities import emptyelement
                                        emptyelement.type_element("By.XPATH","xpath",f"//textarea[@placeholder='Add comments about this patient']",4,driver,"Empty Comment Area")
                                        time.sleep(4)
                                        from droid_activities import TypeElement
                                        TypeElement.type_element("By.XPATH", "xpath",f"//textarea[@placeholder='Add comments about this patient']",f"DC if not scheduled {Onemonth_date}",1,driver,"Add comments")
                                        # from droid_activities import ClickElement
                                        # ClickElement.click_element("By.XPATH", "xpath",f"//div[contains(@class, 'cursor-pointer') and .//span[normalize-space(.)='Save']]",1," Click Save",driver)
                                        time.sleep(4)
                                        ClickElement.click_element("By.XPATH", "xpath",f"//button[.//span[normalize-space(.)='Close']]",1," Click Close",driver)
                                        from droid_activities import excelappend
                                        excelappend.append_excel('C:\\RisePT\\Daily Summary Folder'+'\\'+'RisePT_PatientCoordination_SummaryReport - '+currentdate.replace('-','.')+'.xlsx', [currentdate,"N/A","N/A",Fname+" "+Lname,DOB_4th,"N/A","N/A",'Success','The patient has been moved from Followups to Last Discharge'], 'Sheet1')
                                        Loop_Count=Loop_Count+1
                                    else: # Patients Has Active Campaine
                                        time.sleep(1)
                                        from droid_activities import windowhandle
                                        switch_to_window_by_title(driver, "prompt")
                                        time.sleep(3)
                                        from droid_activities import ClickElement
                                        ClickElement.click_element("By.XPATH", "xpath",f"//a[.//div[normalize-space()='Patients']]",1,"Patients Menu",driver)
                                        from droid_activities import hoverElement
                                        hoverElement.hover_element("By.XPATH", "xpath",f"//input[@*='Search patients'][@type='search']",1,"Patient Name Text Field",driver)
                                        time.sleep(1)
                                        from droid_activities import ClickElement
                                        ClickElement.click_element("By.XPATH", "xpath",f"//input[@*='Search patients'][@type='search']",1,"patient Name text field",driver)
                                        from droid_activities import emptyelement
                                        emptyelement.type_element("By.XPATH","xpath",f"//input[@*='Search patients'][@type='search']",1,driver,"Patient Name Text Field")
                                        import time
                                        time.sleep(1)
                                        from droid_activities import TypeElement
                                        TypeElement.type_element("By.XPATH", "xpath",f"//input[@*='Search patients'][@type='search']",FollowUp_Patient_PNO,1,driver,"Type Patient Phone Number")
                                        import time
                                        time.sleep(1)
                                        from droid_activities import ElementWait
                                        Patient_notexist = ElementWait.element_wait(driver, "By.XPATH", f"//div[contains(@class,'text-p-gray600')]//div[contains(.,'No results, try searching')]",10)
                                        if(Patient_notexist == True):
                                            from droid_activities import ClickElement
                                            ClickElement.click_element("By.XPATH", "xpath",f"//div[contains(@class,'p-listview')]//button[contains(@class,'outline-p-blue600')]",1,"ADD PAtients Button",driver)
                                            import time
                                            time.sleep(3)
                                            from droid_activities import ClickElement
                                            ClickElement.click_element("By.XPATH", "xpath",f"//input[@data-testid='patient-firstname']",1,"First Name field",driver)
                                            from droid_activities import TypeElement
                                            TypeElement.type_element("By.XPATH", "xpath",f"//input[@data-testid='patient-firstname']",Fname,1,driver,"Type First Name")
                                            from droid_activities import ClickElement
                                            ClickElement.click_element("By.XPATH", "xpath",f"//input[@data-testid='patient-lastname']",1,"Last Name field",driver)
                                            from droid_activities import TypeElement
                                            TypeElement.type_element("By.XPATH", "xpath",f"//input[@data-testid='patient-lastname']",Lname,1,driver,"Type Last Name")
                                            from droid_activities import ClickElement
                                            ClickElement.click_element("By.XPATH", "xpath",f"//input[@data-testid='patient-dateofbirth']",1,"Date of Birth field",driver)
                                            from droid_activities import TypeElement
                                            TypeElement.type_element("By.XPATH", "xpath",f"//input[@data-testid='patient-dateofbirth']",DOB_4th,1,driver,"Type Date of Birth")
                                            try:
                                                from droid_activities import ClickElement
                                                ClickElement.click_element("By.XPATH", "xpath",f"//div[@data-testid='patient-gender']",1,"Gender field",driver)
                                            except:
                                                time.sleep(5)
                                            from droid_activities import ClickElement
                                            ClickElement.click_element("By.XPATH", "xpath",f"//div[@role='option']//span[text()='Female']",1,"Click Female",driver)
                                            from droid_activities import ClickElement
                                            ClickElement.click_element("By.XPATH", "xpath",f"//input[@aria-label='Mobile Phone *']",1,"Mobile Phone field",driver)
                                            from droid_activities import TypeElement
                                            TypeElement.type_element("By.XPATH", "xpath",f"//input[@aria-label='Mobile Phone *']",FollowUp_Patient_PNO,1,driver,"Type Mobile Phone ")
                                            from droid_activities import ClickElement
                                            ClickElement.click_element("By.XPATH", "xpath",f"//button[.//span[normalize-space()='Create Patient']]",1,"Click Create Patients",driver)
                                            time.sleep(5)
                                        try:
                                            from droid_activities import ClickElement
                                            ClickElement.click_element("By.XPATH", "xpath",f"//div[contains(@class, 'text-weight-medium') and contains(@class, 'text-subtitle1')]",1,"Patient Profile",driver)
                                        except:
                                            print(" Patients Not found")
                                        from droid_activities import hoverElement
                                        hoverElement.hover_element("By.XPATH", "xpath",f"//div[contains(@class,'q-chip')][.//div[normalize-space()='Visits']]",1,"Visits",driver)
                                        from droid_activities import ClickElement
                                        ClickElement.click_element("By.XPATH", "xpath",f"//div[contains(@class,'q-chip')][.//div[normalize-space()='Visits']]",1,"Visits Menu",driver)
                                        time.sleep(3)
                                        from datetime import datetime, timedelta
                                        def add_business_days(start_date, days=1):
                                            current = start_date
                                            added = 0
                                            while added < days:
                                                current += timedelta(days=1)
                                                if current.weekday() < 5:  # Monday=0 … Friday=4
                                                    added += 1
                                            return current
                                        today = datetime.today()
                                        Upcoming_Date = add_business_days(today)
                                        Upcoming_Date=Upcoming_Date.strftime("%m/%d/%Y")
                                        print(Upcoming_Date)
                                        from droid_activities import GetTextElement 
                                        Get_future= GetTextElement.get_textElement("By.XPATH",f"//div[normalize-space(text())='Future']/following-sibling::div[normalize-space()]",1,"Get Future",driver)
                                        print(Get_future)
                                        Get_future=int(Get_future)
                                        from droid_activities import ElementWait
                                        visit_missing = ElementWait.element_wait(driver, "By.XPATH", f"//i[@class='p-pa-xs q-icon text-p-red600 mdi mdi-alert-outline']",10)
                                        Get_All= GetTextElement.get_textElement("By.XPATH",f"//button[.//div[normalize-space()='All']]//div[contains(@class,'bg-p')]",1,"Get All",driver)
                                        print(Get_All)
                                        from droid_activities import ElementWait
                                        No_Visits = ElementWait.element_wait(driver, "By.XPATH", f"//*[contains(@class,'bg-p-red50')]//*[contains(@class,'omni-type-medium')]",10)
                                        print(No_Visits)
                                        Get_All=int(Get_All)
                                        from droid_activities import GetTextElement 
                                        Get_future= GetTextElement.get_textElement("By.XPATH",f"//div[normalize-space()='Future']/following-sibling::div[1]",1,"Get Future",driver)
                                        print(Get_future)
                                        Get_future=int(Get_future)
                                        if Get_future <= 0:
                                            from droid_activities import ClickElement
                                            ClickElement.click_element("By.XPATH", "xpath",f"(//button[.//i[contains(@class,'mdi-checkbox-marked-circle-plus-outline')]])[2]",4,"Click Task Button",driver)
                                            time.sleep(2)
                                            from droid_activities import ClickElement
                                            ClickElement.click_element("By.XPATH", "xpath",f"//button[.//div[normalize-space(text())='Add New Task']]",4,"Click Add New Button",driver)
                                            from droid_activities import ClickElement
                                            ClickElement.click_element("By.XPATH", "xpath",f"//input[@placeholder='Add title']",4,"Click Add title",driver)
                                            from droid_activities import emptyelement
                                            emptyelement.type_element("By.XPATH","xpath",f"//input[@placeholder='Add title']",1,driver,"Add title Empty")
                                            from droid_activities import TypeElement
                                            TypeElement.type_element("By.XPATH", "xpath",f"//input[@placeholder='Add title']","2 Schedule Eval",1,driver,"Type 2 Schedule Eval Patient")
                                            from droid_activities import ClickElement
                                            ClickElement.click_element("By.XPATH", "xpath",f"//textarea[@aria-label='Description']",4,"Click Add title",driver)
                                            from droid_activities import emptyelement
                                            emptyelement.type_element("By.XPATH","xpath",f"//textarea[@aria-label='Description']",1,driver,"Add title Empty")
                                            from droid_activities import TypeElement
                                            TypeElement.type_element("By.XPATH", "xpath",f"//textarea[@aria-label='Description']",f" {Get_FUComments}",1,driver,"Type OAR Patient")
                                            from droid_activities import ClickElement
                                            ClickElement.click_element("By.XPATH", "xpath",f"//div[contains(@class,'q-field__control-container') and .//div[normalize-space(text())='Due Date']]//input",4,"Click Due Date",driver)
                                            from droid_activities import ClickElement
                                            ClickElement.click_element("By.XPATH", "xpath",f"//div[contains(@class,'q-field__control-container') and .//div[normalize-space(text())='Due Date']]//input",4,"Click Due Date",driver)
                                            from droid_activities import emptyelement
                                            emptyelement.type_element("By.XPATH","xpath",f"//div[contains(@class,'q-field__control-container') and .//div[normalize-space(text())='Due Date']]//input",1,driver,"Due Date")
                                            import keyboard;keyboard.press_and_release('enter')
                                            from droid_activities import TypeElement
                                            TypeElement.type_element("By.XPATH", "xpath",f"//input[@aria-label='Due Date' and @placeholder='Select date']",Upcoming_Date,1,driver,"Due Date")
                                            from droid_activities import ClickElement
                                            ClickElement.click_element("By.XPATH", "xpath",f"//div[@role='radio' and @aria-label='High']",4,"Click High",driver) #Manual
                                            import time
                                            time.sleep(1)
                                            from droid_activities import hoverElement
                                            hoverElement.hover_element("By.XPATH", "xpath",f"//label[.//div[normalize-space(text())='Assign to someone']]",2,"Assign to someone",driver)
                                            from droid_activities import ClickElement
                                            ClickElement.click_element("By.XPATH", "xpath",f"//label[.//div[normalize-space(text())='Assign to someone']]",4,"Click Assign to someone",driver)
                                            from droid_activities import TypeElement
                                            TypeElement.type_element("By.XPATH", "xpath",f"//input[@placeholder='Search' and @type='search']","jen simpson",1,driver,"Select assignee")
                                            from droid_activities import ClickElement
                                            ClickElement.click_element("By.XPATH", "xpath",f"//div[contains(@class,'p-select__option-title') and normalize-space()='Jen Simpson']",4,"ClickJen Simpson",driver)
                                            from droid_activities import ClickElement
                                            ClickElement.click_element("By.XPATH", "xpath",f"//button[.//div[normalize-space(.)='Save Task']]",4,"Click Save Task",driver)
                                            from droid_activities import ClickElement
                                            ClickElement.click_element("By.XPATH", "xpath",f"//div[.//div[text()='Task List']]//button[.//i[text()='close']]",4,"Click Close Button",driver)
                                            time.sleep(3)
                                            from droid_activities import windowhandle
                                            windowhandle.window_handle(driver,2)
                                            from droid_activities import ClickElement
                                            ClickElement.click_element("By.XPATH", "xpath",f"(//button[@aria-haspopup='menu' and normalize-space()='Actions'])[2]",3,"Click Action",driver)
                                            ClickElement.click_element("By.XPATH", "xpath",f"//div[@role='menuitem' and contains(., 'Remove from Workflow')]",3,"Click Case not used",driver)
                                            #ClickElement.click_element("By.XPATH", "xpath",f"//button[.//span[normalize-space(.)='Close']]",1," Click Close",driver)
                                            from droid_activities import excelappend
                                            excelappend.append_excel('C:\\RisePT\\Daily Summary Folder'+'\\'+'RisePT_PatientCoordination_SummaryReport - '+currentdate.replace('-','.')+'.xlsx', [currentdate,"N/A","Followups",Fname+" "+Lname,DOB_4th,"N/A","N/A",'Success','This patient has been assigned a task and removed from the workflow'], 'Sheet1')
                                            Loop_Count=Loop_Count+1
                                        else: #Future Available
                                            print("Future Available")
                                            time.sleep(3)
                                            from droid_activities import windowhandle
                                            windowhandle.window_handle(driver,2)
                                            from droid_activities import ClickElement
                                            ClickElement.click_element("By.XPATH", "xpath",f"(//button[@aria-haspopup='menu' and normalize-space()='Actions'])[2]",3,"Click Action",driver)
                                            ClickElement.click_element("By.XPATH", "xpath",f"//div[@role='menuitem' and contains(., 'Remove from Workflow')]",3,"Click Case not used",driver)
                                            #ClickElement.click_element("By.XPATH", "xpath",f"//button[.//span[normalize-space(.)='Close']]",1," Click Close",driver)
                                            from droid_activities import excelappend
                                            excelappend.append_excel('C:\\RisePT\\Daily Summary Folder'+'\\'+'RisePT_PatientCoordination_SummaryReport - '+currentdate.replace('-','.')+'.xlsx', [currentdate,"N/A","Followups",Fname+" "+Lname,DOB_4th,"N/A","N/A",'Success','This patient Move to the Schedule Patients workflow'], 'Sheet1')
                                            Loop_Count=Loop_Count+1  
                                else:# API or Form Are Not Available
                                    import time
                                    time.sleep(3)
                                    from droid_activities import message_box_delay
                                    message_box_delay.show_timed_message_box('No Launch Page Exist -PatientHeader', 1)
                                    ClickElement.click_element("By.XPATH", "xpath",f"//button[.//span[normalize-space(.)='Close']]",1," Click Close",driver)
                                    from droid_activities import excelappend
                                    excelappend.append_excel('C:\\RisePT\\Daily Summary Folder'+'\\'+'RisePT_PatientCoordination_SummaryReport - '+currentdate.replace('-','.')+'.xlsx', [currentdate,"N/A","Follow ups Patients",Fname+" "+Lname,DOB_4th,"N/A","N/A",'Needs Attention','Two Outgoing Call are Not Available, so skipped this patient'], 'Sheet1')
                                    Loop_Count=Loop_Count+1
                            else: #Else Start - Not Valid Out Going Call 
                                import time
                                time.sleep(3)
                                from droid_activities import message_box_delay
                                message_box_delay.show_timed_message_box('No Launch Page Exist -PatientHeader', 1)
                                ClickElement.click_element("By.XPATH", "xpath",f"//button[.//span[normalize-space(.)='Close']]",1," Click Close",driver)
                                from droid_activities import excelappend
                                excelappend.append_excel('C:\\RisePT\\Daily Summary Folder'+'\\'+'RisePT_PatientCoordination_SummaryReport - '+currentdate.replace('-','.')+'.xlsx', [currentdate,"N/A","Follow ups Patients",Fname+" "+Lname,DOB_4th,"N/A","N/A",'Needs Attention','This patient outgoing call validation has failed, so skipped this patient'], 'Sheet1')
                                Loop_Count=Loop_Count+1
                        else:
                            print(" Completed")
                            break
                    else: #else for While loop break condition for Follow Up call column
                        print("All the Valid Follow Up patients are Completed")
                        break 
                except:
                    print("Except Follow up Call")
                    import traceback
                    Er = traceback.format_exc()
                    print(f"An error occurred: {Er}") 
                    time.sleep(2)          
                #<--------------- Follow ups End ----------------------------->
                #<----------------------- OAR Starting  -------------------------------->
                try:
                    time.sleep(5)
                    from droid_activities import date_time
                    currentdate = date_time.date_time('%m-%d-%Y', 'current',0, "currentdate","currentdate")
                    from droid_activities import FileExists
                    from droid_activities import windowhandle
                    windowhandle.window_handle(driver,2)
                    from droid_activities import hoverElement
                    hoverElement.hover_element("By.XPATH", "xpath",f"//div[contains(@class, 'inline-flex')]/h2[contains(text(), 'OAR')]",1,"OAR",driver)
                    time.sleep(1)
                    from droid_activities import ClickElement
                    ClickElement.click_element("By.XPATH", "xpath",f"//div[contains(@class, 'inline-flex')]/h2[contains(text(), 'OAR')]",1," Click OAR ",driver)
                    time.sleep(1)
                    from droid_activities import GetTextElement
                    OAR_Paientscount = GetTextElement.get_textElement("By.XPATH",f"//div[@class='flex items-center justify-between mb-4'] [.//h2[normalize-space(text())='OAR']] /div[contains(@class,'inline-flex') and contains(@class,'font-semibold')]",1,"Get 4th attempt Count",driver)
                    #print(attempt_4thcount)
                    phone_numbers = []
                    OAR_Paientscount=int(OAR_Paientscount)
                    print(OAR_Paientscount)
                    Loop_Count=1
                    Increment_number=1
                    while(True):
                        if(OAR_Paientscount>=Loop_Count):
                            from droid_activities import ClickElement
                            time.sleep(3)
                            while(True):
                                try:
                                    from droid_activities import hoverElement
                                    hoverElement.hover_element("By.XPATH", "xpath",f"(//h2[normalize-space()='OAR']  /following::div[@role='button' and @aria-roledescription='draggable'])[{Increment_number}]",5,"Click OAR Patients",driver)
                                    time.sleep(2)
                                    ClickElement.click_element("By.XPATH", "xpath",f"(//h2[normalize-space()='OAR']  /following::div[@role='button' and @aria-roledescription='draggable'])[{Increment_number}]",5," Click OAR Patients",driver)
                                    break
                                except:
                                    from droid_activities import hoverElement
                                    hoverElement.hover_element("By.XPATH", "xpath",f"//h2[text()='OAR']/ancestor::div[contains(@class, 'flex items-center')]//following-sibling::div//button[contains(text(), 'Load More')]",1,"Load more for OAR",driver)
                                    time.sleep(1)
                                    ClickElement.click_element("By.XPATH", "xpath",f"//h2[text()='OAR']/ancestor::div[contains(@class, 'flex items-center')]//following-sibling::div//button[contains(text(), 'Load More')]",5,"OAR  Click Load More Button",driver)# need to add click extra patient step
                                    time.sleep(2)
                                    print("click extra patinents") # need to add click extra patient step
                            while(True):
                                from droid_activities import ElementWait
                                PatientDetails_exist = ElementWait.element_wait(driver, "By.XPATH", f"//button[@role='tab' and normalize-space()='Patient Details']",10)
                                if(PatientDetails_exist == True):
                                    break
                                else:
                                    time.sleep(5)
                            time.sleep(2)
                            from droid_activities import GetTextElement
                            OAR_PatientsPNO = GetTextElement.get_textElement("By.XPATH",f"//div[contains(@aria-label, 'Phone Number')]",1,"Get DOB",driver)
                            if (Loop_Count >= 2):
                                if OAR_PatientsPNO in phone_numbers:
                                    Increment_number = Increment_number+1
                                    ClickElement.click_element("By.XPATH", "xpath",f"//button[.//span[normalize-space(.)='Close']]",1," Click Close",driver)
                                    continue
                            phone_numbers.append(OAR_PatientsPNO)
                            from droid_activities import ElementWait
                            PatientDetails_exist = ElementWait.element_wait(driver, "By.XPATH", f"//button[@role='tab' and normalize-space()='Patient Details']",10)
                            launchcount = int(0) #int
                            if PatientDetails_exist == True: #range
                                from droid_activities import message_box_delay
                                message_box_delay.show_timed_message_box('Launch Page Exist - PatientHeader', 1)
                                from droid_activities import ClickElement
                                ClickElement.click_element("By.XPATH", "xpath",f"//button[@role='tab' and contains(normalize-space(.), 'Patient Details')]",1," Click Patient Details",driver)
                                from droid_activities import GetTextElement
                                OAR_Fname = GetTextElement.get_textElement("By.XPATH",f"//div[@role='button'][contains(@aria-label, 'First Name')]",1,"First Name",driver)
                                print(OAR_Fname)
                                from droid_activities import GetTextElement
                                OAR_Lname = GetTextElement.get_textElement("By.XPATH",f"//div[@role='button'][contains(@aria-label, 'Last Name')]",1,"Last Name",driver)
                                print(OAR_Lname)
                                from droid_activities import GetTextElement
                                OAR_DOB = GetTextElement.get_textElement("By.XPATH",f"//div[@role='button'][contains(@aria-label, 'Date of Birth')]",1,"Get DOB",driver)
                                print(OAR_DOB)
                                from droid_activities import GetTextElement
                                Get_Tag = GetTextElement.get_textElement("By.XPATH",f"//*[@role='button' and contains(@aria-label,'Tags')]",1,"Get Tag",driver)
                                print(Get_Tag)
                                if(Get_Tag == "Active Campaign"):
                                    print(" Active Compaine Are Available")
                                else:
                                    print("Active compaine not commimg")
                                    import time
                                    time.sleep(3)
                                    from droid_activities import message_box_delay
                                    message_box_delay.show_timed_message_box('No Launch Page Exist -PatientHeader', 1)
                                    ClickElement.click_element("By.XPATH", "xpath",f"//button[.//span[normalize-space(.)='Close']]",1," Click Close",driver)
                                    from droid_activities import excelappend
                                    excelappend.append_excel('C:\\RisePT\\Daily Summary Folder'+'\\'+'RisePT_PatientCoordination_SummaryReport - '+currentdate.replace('-','.')+'.xlsx', [currentdate,"N/A","OAR Patients",OAR_Fname+" "+OAR_Lname,OAR_DOB,"N/A","N/A",'Needs Attention','Not Active Compaine'], 'Sheet1')
                                    Loop_Count=Loop_Count+1
                                    continue
                                time.sleep(5)
                                from droid_activities import ClickElement
                                from selenium.webdriver.common.by import By
                                from selenium.webdriver.support.ui import WebDriverWait
                                from selenium.webdriver.support import expected_conditions as EC
                                from datetime import datetime
                                # ---------- FIRST OUTGOING CALL ----------
                                xpath1 = "(//div[.//div[normalize-space()='Outgoing Call']]//div[@data-date])[1]"
                                from droid_activities import ElementWait
                                Firstoutgoingcall_exist = ElementWait.element_wait(driver, "By.XPATH", f"{xpath1}",10)
                                if(Firstoutgoingcall_exist):   
                                    elem1 = driver.find_element(By.XPATH, xpath1)    
                                    date_text_1 = elem1.get_attribute("data-date")  # best option
                                    print(date_text_1)
                                    OutDate_1 = datetime.strptime(date_text_1, "%A, %B %d")  
                                else:
                                    import time
                                    time.sleep(3)
                                    from droid_activities import message_box_delay
                                    message_box_delay.show_timed_message_box('No Launch Page Exist -PatientHeader', 1)
                                    ClickElement.click_element("By.XPATH", "xpath",f"//button[.//span[normalize-space(.)='Close']]",1," Click Close",driver)
                                    from droid_activities import excelappend
                                    excelappend.append_excel('C:\\RisePT\\Daily Summary Folder'+'\\'+'RisePT_PatientCoordination_SummaryReport - '+currentdate.replace('-','.')+'.xlsx', [currentdate,"N/A","OAR Patients",OAR_Fname+" "+OAR_Lname,OAR_DOB,"N/A","N/A",'Needs Attention','No Outging Call'], 'Sheet1')
                                    Loop_Count=Loop_Count+1
                                    continue
                                # ---------- SECOND OUTGOING CALL ----------
                                xpath2 = "(//div[.//div[normalize-space()='Outgoing Call']]//div[@data-date])[2]"
                                from droid_activities import ElementWait
                                Secondoutgoingcall_exist = ElementWait.element_wait(driver, "By.XPATH", f"{xpath2}",10)
                                if(Secondoutgoingcall_exist): 
                                    elem2 = driver.find_element(By.XPATH, xpath2)    
                                    date_text_2 = elem2.get_attribute("data-date")
                                    print(date_text_2)
                                    OutDate_2 = datetime.strptime(date_text_2, "%A, %B %d")
                                    difference = abs((OutDate_2 - OutDate_1).days)
                                else:
                                    print("Only One Call Available")
                                time.sleep(2)
                                ClickElement.click_element("By.XPATH", "xpath",f"//button[@role='tab' and contains(normalize-space(.), 'Patient Details')]",1," Click Patient Details",driver)
                                from droid_activities import hoverElement
                                hoverElement.hover_element("By.XPATH", "xpath",f"//h3[normalize-space()='Additional Details']",1,"Hover additional-information",driver)
                                from droid_activities import ClickElement
                                ClickElement.click_element("By.XPATH", "xpath",f"//h3[normalize-space()='Additional Details']",1," Click additional-information",driver)
                                from droid_activities import GetTextElement
                                Get_Comments = GetTextElement.get_textElement("By.XPATH",f"//*[@role='button' and contains(@aria-label,'Comments')]",1,"Get OAR Comments",driver)
                                time.sleep(1)
                                from droid_activities import windowhandle
                                switch_to_window_by_title(driver, "prompt")
                                time.sleep(3)
                                from droid_activities import ClickElement
                                ClickElement.click_element("By.XPATH", "xpath",f"//a[.//div[normalize-space()='Patients']]",1,"Patients Menu",driver)
                                from droid_activities import hoverElement
                                hoverElement.hover_element("By.XPATH", "xpath",f"//input[@*='Search patients'][@type='search']",1,"Patient Name Text Field",driver)
                                time.sleep(1)
                                from droid_activities import ClickElement
                                ClickElement.click_element("By.XPATH", "xpath",f"//input[@*='Search patients'][@type='search']",1,"patient Name text field",driver)
                                from droid_activities import emptyelement
                                emptyelement.type_element("By.XPATH","xpath",f"//input[@*='Search patients'][@type='search']",1,driver,"Patient Name Text Field")
                                import time
                                time.sleep(1)
                                from droid_activities import TypeElement
                                TypeElement.type_element("By.XPATH", "xpath",f"//input[@*='Search patients'][@type='search']",OAR_PatientsPNO,1,driver,"Type Patient Phone Number")
                                import time
                                time.sleep(1)
                                from droid_activities import ElementWait
                                Patient_notexist = ElementWait.element_wait(driver, "By.XPATH", f"//div[contains(@class,'text-p-gray600')]//div[contains(.,'No results, try searching')]",10)
                                if(Patient_notexist == True):
                                    from droid_activities import ClickElement
                                    ClickElement.click_element("By.XPATH", "xpath",f"//div[contains(@class,'p-listview')]//button[contains(@class,'outline-p-blue600')]",1,"ADD PAtients Button",driver)
                                    import time
                                    time.sleep(3)
                                    from droid_activities import ClickElement
                                    ClickElement.click_element("By.XPATH", "xpath",f"//input[@data-testid='patient-firstname']",1,"First Name field",driver)
                                    from droid_activities import TypeElement
                                    TypeElement.type_element("By.XPATH", "xpath",f"//input[@data-testid='patient-firstname']",OAR_Fname,1,driver,"Type First Name")
                                    from droid_activities import ClickElement
                                    ClickElement.click_element("By.XPATH", "xpath",f"//input[@data-testid='patient-lastname']",1,"Last Name field",driver)
                                    from droid_activities import TypeElement
                                    TypeElement.type_element("By.XPATH", "xpath",f"//input[@data-testid='patient-lastname']",OAR_Lname,1,driver,"Type Last Name")
                                    from droid_activities import ClickElement
                                    ClickElement.click_element("By.XPATH", "xpath",f"//input[@data-testid='patient-dateofbirth']",1,"Date of Birth field",driver)
                                    from droid_activities import TypeElement
                                    TypeElement.type_element("By.XPATH", "xpath",f"//input[@data-testid='patient-dateofbirth']",OAR_DOB,1,driver,"Type Date of Birth")
                                    try:
                                        from droid_activities import ClickElement
                                        ClickElement.click_element("By.XPATH", "xpath",f"//div[@data-testid='patient-gender']",1,"Gender field",driver)
                                    except:
                                        time.sleep(5)
                                    from droid_activities import ClickElement
                                    ClickElement.click_element("By.XPATH", "xpath",f"//div[@role='option']//span[text()='Female']",1,"Click Female",driver)
                                    from droid_activities import ClickElement
                                    ClickElement.click_element("By.XPATH", "xpath",f"//input[@aria-label='Mobile Phone *']",1,"Mobile Phone field",driver)
                                    from droid_activities import TypeElement
                                    TypeElement.type_element("By.XPATH", "xpath",f"//input[@aria-label='Mobile Phone *']",OAR_PatientsPNO,1,driver,"Type Mobile Phone ")
                                    from droid_activities import ClickElement
                                    ClickElement.click_element("By.XPATH", "xpath",f"//button[.//span[normalize-space()='Create Patient']]",1,"Click Create Patients",driver)
                                    time.sleep(5)
                                try:
                                    from droid_activities import ClickElement
                                    ClickElement.click_element("By.XPATH", "xpath",f"//div[contains(@class, 'text-weight-medium') and contains(@class, 'text-subtitle1')]",1,"Patient Profile",driver)
                                except:
                                    print(" Patients Not found")
                                from droid_activities import hoverElement
                                hoverElement.hover_element("By.XPATH", "xpath",f"//div[contains(@class,'q-chip')][.//div[normalize-space()='Visits']]",1,"Visits",driver)
                                from droid_activities import ClickElement
                                ClickElement.click_element("By.XPATH", "xpath",f"//div[contains(@class,'q-chip')][.//div[normalize-space()='Visits']]",1,"Visits Menu",driver)
                                time.sleep(3)
                                from datetime import datetime, timedelta
                                def add_business_days(start_date, days=2):
                                    current = start_date
                                    added = 0
                                    while added < days:
                                        current += timedelta(days=1)
                                        if current.weekday() < 5:  # Monday=0 … Friday=4
                                            added += 1
                                    return current
                                today = datetime.today()
                                Upcoming_Date = add_business_days(today)
                                Upcoming_Date=Upcoming_Date.strftime("%m/%d/%Y")
                                print(Upcoming_Date)
                                from droid_activities import GetTextElement 
                                Get_future= GetTextElement.get_textElement("By.XPATH",f"//div[normalize-space(text())='Future']/following-sibling::div[normalize-space()]",1,"Get Future",driver)
                                print(Get_future)
                                Get_future=int(Get_future)
                                from droid_activities import ElementWait
                                visit_missing = ElementWait.element_wait(driver, "By.XPATH", f"//i[@class='p-pa-xs q-icon text-p-red600 mdi mdi-alert-outline']",10)
                                Get_All= GetTextElement.get_textElement("By.XPATH",f"//button[.//div[normalize-space()='All']]//div[contains(@class,'bg-p')]",1,"Get All",driver)
                                print(Get_All)
                                from droid_activities import ElementWait
                                No_Visits = ElementWait.element_wait(driver, "By.XPATH", f"//*[contains(@class,'bg-p-red50')]//*[contains(@class,'omni-type-medium')]",10)
                                print(No_Visits)
                                Get_All=int(Get_All)
                                from droid_activities import GetTextElement 
                                Get_future= GetTextElement.get_textElement("By.XPATH",f"//div[normalize-space()='Future']/following-sibling::div[1]",1,"Get Future",driver)
                                print(Get_future)
                                Get_future=int(Get_future)
                                if Get_future <= 0:
                                    from droid_activities import ClickElement
                                    ClickElement.click_element("By.XPATH", "xpath",f"(//button[.//i[contains(@class,'mdi-checkbox-marked-circle-plus-outline')]])[2]",4,"Click Task Button",driver)
                                    time.sleep(2)
                                    from droid_activities import ClickElement
                                    ClickElement.click_element("By.XPATH", "xpath",f"//button[.//div[normalize-space(text())='Add New Task']]",4,"Click Add New Button",driver)
                                    from droid_activities import ClickElement
                                    ClickElement.click_element("By.XPATH", "xpath",f"//input[@placeholder='Add title']",4,"Click Add title",driver)
                                    from droid_activities import emptyelement
                                    emptyelement.type_element("By.XPATH","xpath",f"//input[@placeholder='Add title']",1,driver,"Add title Empty")
                                    if(Firstoutgoingcall_exist == True):
                                        from droid_activities import TypeElement
                                        TypeElement.type_element("By.XPATH", "xpath",f"//input[@placeholder='Add title']","2 Schedule Eval",1,driver,"Type 2 Schedule Eval Patient")
                                    elif(Secondoutgoingcall_exist == True):
                                        from droid_activities import TypeElement
                                        TypeElement.type_element("By.XPATH", "xpath",f"//input[@placeholder='Add title']","3 Schedule Eval",1,driver,"Type 3 Schedule Eval Patient")
                                    from droid_activities import ClickElement
                                    ClickElement.click_element("By.XPATH", "xpath",f"//textarea[@aria-label='Description']",4,"Click Add title",driver)
                                    from droid_activities import emptyelement
                                    emptyelement.type_element("By.XPATH","xpath",f"//textarea[@aria-label='Description']",1,driver,"Add title Empty")
                                    from droid_activities import TypeElement
                                    TypeElement.type_element("By.XPATH", "xpath",f"//textarea[@aria-label='Description']",f"OAR - {Get_Comments}",1,driver,"Type OAR Patient")
                                    from droid_activities import ClickElement
                                    ClickElement.click_element("By.XPATH", "xpath",f"//div[contains(@class,'q-field__control-container') and .//div[normalize-space(text())='Due Date']]//input",4,"Click Due Date",driver)
                                    from droid_activities import ClickElement
                                    ClickElement.click_element("By.XPATH", "xpath",f"//div[contains(@class,'q-field__control-container') and .//div[normalize-space(text())='Due Date']]//input",4,"Click Due Date",driver)
                                    from droid_activities import emptyelement
                                    emptyelement.type_element("By.XPATH","xpath",f"//div[contains(@class,'q-field__control-container') and .//div[normalize-space(text())='Due Date']]//input",1,driver,"Due Date")
                                    import keyboard;keyboard.press_and_release('enter')
                                    from droid_activities import TypeElement
                                    TypeElement.type_element("By.XPATH", "xpath",f"//input[@aria-label='Due Date' and @placeholder='Select date']",Upcoming_Date,1,driver,"Due Date")
                                    from droid_activities import ClickElement
                                    ClickElement.click_element("By.XPATH", "xpath",f"//div[@role='radio' and @aria-label='High']",4,"Click High",driver) #Manual
                                    import time
                                    time.sleep(1)
                                    from droid_activities import hoverElement
                                    hoverElement.hover_element("By.XPATH", "xpath",f"//label[.//div[normalize-space(text())='Assign to someone']]",2,"Assign to someone",driver)
                                    from droid_activities import ClickElement
                                    ClickElement.click_element("By.XPATH", "xpath",f"//label[.//div[normalize-space(text())='Assign to someone']]",4,"Click Assign to someone",driver)
                                    from droid_activities import TypeElement
                                    TypeElement.type_element("By.XPATH", "xpath",f"//input[@placeholder='Search' and @type='search']","jen simpson",1,driver,"Select assignee")
                                    from droid_activities import ClickElement
                                    ClickElement.click_element("By.XPATH", "xpath",f"//div[contains(@class,'p-select__option-title') and normalize-space()='Jen Simpson']",4,"ClickJen Simpson",driver)
                                    from droid_activities import ClickElement
                                    ClickElement.click_element("By.XPATH", "xpath",f"//button[.//div[normalize-space(.)='Save Task']]",4,"Click Save Task",driver)
                                    from droid_activities import ClickElement
                                    ClickElement.click_element("By.XPATH", "xpath",f"//div[.//div[text()='Task List']]//button[.//i[text()='close']]",4,"Click Close Button",driver)
                                    time.sleep(3)
                                    from droid_activities import windowhandle
                                    windowhandle.window_handle(driver,2)
                                    from droid_activities import ClickElement
                                    ClickElement.click_element("By.XPATH", "xpath",f"(//button[@aria-haspopup='menu' and normalize-space()='Actions'])[2]",3,"Click Action",driver)
                                    ClickElement.click_element("By.XPATH", "xpath",f"//div[@role='menuitem' and contains(., 'Remove from Workflow')]",3,"Click Case not used",driver)
                                    #ClickElement.click_element("By.XPATH", "xpath",f"//button[.//span[normalize-space(.)='Close']]",1," Click Close",driver)
                                    from droid_activities import excelappend
                                    excelappend.append_excel('C:\\RisePT\\Daily Summary Folder'+'\\'+'RisePT_PatientCoordination_SummaryReport - '+currentdate.replace('-','.')+'.xlsx', [currentdate,"N/A","OAR Patients",OAR_Fname+" "+OAR_Lname,OAR_DOB,"N/A","N/A",'Success','This patient has been assigned a task and removed from the workflow'], 'Sheet1')
                                    Loop_Count=Loop_Count+1
                                else: # Visits are Available so go to the solumn then remove work flow
                                    import time
                                    time.sleep(3)
                                    from droid_activities import windowhandle
                                    windowhandle.window_handle(driver,2)
                                    from droid_activities import ClickElement
                                    ClickElement.click_element("By.XPATH", "xpath",f"(//button[@aria-haspopup='menu' and normalize-space()='Actions'])[2]",3,"Click Action",driver)
                                    ClickElement.click_element("By.XPATH", "xpath",f"//div[@role='menuitem' and contains(., 'Remove from Workflow')]",3,"Click Case not used",driver)
                                    #ClickElement.click_element("By.XPATH", "xpath",f"//button[.//span[normalize-space(.)='Close']]",1," Click Close",driver)
                                    from droid_activities import excelappend
                                    excelappend.append_excel('C:\\RisePT\\Daily Summary Folder'+'\\'+'RisePT_PatientCoordination_SummaryReport - '+currentdate.replace('-','.')+'.xlsx', [currentdate,"N/A","OAR Patients",OAR_Fname+" "+OAR_Lname,OAR_DOB,"N/A","N/A",'Success','This patient has been removed from the workflow'], 'Sheet1')
                                    Loop_Count=Loop_Count+1
                                # else: #Out going call Invalid
                                #     import time
                                #     time.sleep(3)
                                #     from droid_activities import message_box_delay
                                #     message_box_delay.show_timed_message_box('No Launch Page Exist -PatientHeader', 1)
                                #     ClickElement.click_element("By.XPATH", "xpath",f"//button[.//span[normalize-space(.)='Close']]",1," Click Close",driver)
                                #     from droid_activities import excelappend
                                #     excelappend.append_excel('C:\\RisePT\\Daily Summary Folder'+'\\'+'RisePT_PatientCoordination_SummaryReport - '+currentdate.replace('-','.')+'.xlsx', [currentdate,"N/A","OAR Patients",OAR_Fname+" "+OAR_Lname,OAR_DOB,"N/A","N/A",'Needs Attention','This patient outgoing call validation has failed, so skipped this patient'], 'Sheet1')
                                #     Loop_Count=Loop_Count+1
                            else:  # Patients Not Available
                                print(" Patients Details are not available")
                                from droid_activities import message_box_delay
                                message_box_delay.show_timed_message_box('No Launch Page Exist -PatientHeader', 1)
                                ClickElement.click_element("By.XPATH", "xpath",f"//button[.//span[normalize-space(.)='Close']]",1," Click Close",driver)
                                from droid_activities import excelappend
                                excelappend.append_excel('C:\\RisePT\\Daily Summary Folder'+'\\'+'RisePT_PatientCoordination_SummaryReport - '+currentdate.replace('-','.')+'.xlsx', [currentdate,"N/A","OAR Patients",OAR_Fname+" "+OAR_Lname,OAR_DOB,"N/A","N/A",'Success','The patients workflow has been successfully processed'], 'Sheet1')
                                Loop_Count=Loop_Count+1
                        else: #else for While loop break condition for Follow Up call column
                            print("All the Valid OAR patients are Completed")
                            break
                except:
                    print("OAR Except Part")
                    try:
                        ClickElement.click_element("By.XPATH", "xpath",f"//button[.//span[normalize-space(.)='Close']]",1," Click Close",driver)
                    except:
                        print(" OAR Except")
                    import traceback
                    Er = traceback.format_exc()
                    print(f"An error occurred: {Er}") 
                    time.sleep(2)
                #<----------------------- OAR END  -------------------------------->
                
                #<--------------------------- Schedule Patients Start ------------------------------->
                time.sleep(5)
                try:
                    import time
                    time.sleep(5)
                    from droid_activities import windowhandle
                    windowhandle.window_handle(driver,2)
                    from droid_activities import hoverElement
                    hoverElement.hover_element("By.XPATH", "xpath",f"//div[contains(@class, 'inline-flex')]/h2[contains(text(), 'Scheduled Patients')]",1,"Scheduled Patients",driver)
                    time.sleep(1)
                    from droid_activities import ClickElement
                    ClickElement.click_element("By.XPATH", "xpath",f"//div[contains(@class, 'inline-flex')]/h2[contains(text(), 'Scheduled Patients')]",1," Click Scheduled Patients",driver)
                    time.sleep(1)
                    from droid_activities import GetTextElement
                    Scheduled_Patientcount = GetTextElement.get_textElement("By.XPATH",f"//div[@class='flex items-center justify-between mb-4'] [.//h2[normalize-space(text())='Scheduled Patients']] /div[contains(@class,'inline-flex') and contains(@class,'font-semibold')]",1,"Get Scheduled Patients Count",driver)
                    #print(attempt_4thcount)
                    phone_numbers = []
                    Scheduled_Patientcount=int(Scheduled_Patientcount)
                    print(Scheduled_Patientcount)
                    Loop_Count=1
                    Increment_number=1
                    while(True):
                        if(Scheduled_Patientcount>=Loop_Count):
                            from droid_activities import ClickElement
                            time.sleep(4)
                            while(True):
                                try:
                                    from droid_activities import hoverElement
                                    hoverElement.hover_element("By.XPATH", "xpath",f"(//h2[normalize-space()='Scheduled Patients']  /following::div[@role='button' and @aria-roledescription='draggable'])[{Increment_number}]",1,"Scheduled Patients",driver)
                                    time.sleep(1)
                                    ClickElement.click_element("By.XPATH", "xpath",f"(//h2[normalize-space()='Scheduled Patients']  /following::div[@role='button' and @aria-roledescription='draggable'])[{Increment_number}]",5," Click Scheduled Patients",driver)
                                    break
                                except:
                                    print("click extra patinents") # need to add click extra patient step
                                    from droid_activities import hoverElement
                                    hoverElement.hover_element("By.XPATH", "xpath",f"//h2[text()='Scheduled Patients']/ancestor::div[contains(@class, 'flex items-center')]//following-sibling::div//button[contains(text(), 'Load More')]",1,"Load more for Schedule patients",driver)
                                    time.sleep(1)
                                    ClickElement.click_element("By.XPATH", "xpath",f"//h2[text()='Scheduled Patients']/ancestor::div[contains(@class, 'flex items-center')]//following-sibling::div//button[contains(text(), 'Load More')]",5," Click Load More Button",driver)
                                    time.sleep(3)
                            while(True):
                                from droid_activities import ElementWait
                                PatientDetails_exist = ElementWait.element_wait(driver, "By.XPATH", f"//button[@role='tab' and normalize-space()='Patient Details']",10)
                                if(PatientDetails_exist == True):
                                    break
                                else:
                                    time.sleep(5)
                            from droid_activities import GetTextElement
                            Scheduled_Patients_PNO = GetTextElement.get_textElement("By.XPATH",f"//div[contains(@aria-label, 'Phone Number')]",1,"Get DOB",driver)
                            if (Loop_Count >= 2):
                                if Scheduled_Patients_PNO in phone_numbers:
                                    Increment_number = Increment_number+1
                                    ClickElement.click_element("By.XPATH", "xpath",f"//button[.//span[normalize-space(.)='Close']]",1," Click Close",driver)
                                    continue
                            phone_numbers.append(Scheduled_Patients_PNO)
                            from droid_activities import ElementWait
                            PatientDetails_exist = ElementWait.element_wait(driver, "By.XPATH", f"//button[@role='tab' and normalize-space()='Patient Details']",10)
                            launchcount = int(0) #int
                            if PatientDetails_exist == True: #range
                                from droid_activities import message_box_delay
                                message_box_delay.show_timed_message_box('Launch Page Exist - PatientHeader', 1)
                                from droid_activities import ClickElement
                                #ClickElement.click_element("By.XPATH", "xpath",f"//button[@role='tab' and contains(@id,'trigger-interactions')]",1," Click interactions",driver)
                                from droid_activities import GetTextElement
                                Fname = GetTextElement.get_textElement("By.XPATH",f"//div[@role='button'][contains(@aria-label, 'First Name')]",1,"First Name",driver)
                                print(Fname)
                                from droid_activities import GetTextElement
                                Lname = GetTextElement.get_textElement("By.XPATH",f"//div[@role='button'][contains(@aria-label, 'Last Name')]",1,"Last Name",driver)
                                print(Lname)
                                from droid_activities import GetTextElement
                                DOB_Scheduled = GetTextElement.get_textElement("By.XPATH",f"//div[@role='button'][contains(@aria-label, 'Date of Birth')]",1,"Get DOB",driver)
                                print(DOB_Scheduled)
                                from droid_activities import windowhandle
                                switch_to_window_by_title(driver, "prompt")
                                from droid_activities import ClickElement
                                ClickElement.click_element("By.XPATH", "xpath",f"//a[.//div[normalize-space()='Patients']]",3,"Patients Menu",driver)
                                from droid_activities import hoverElement
                                hoverElement.hover_element("By.XPATH", "xpath",f"//input[@*='Search patients'][@type='search']",1,"Patient Name Text Field",driver)
                                time.sleep(1)
                                from droid_activities import ClickElement
                                ClickElement.click_element("By.XPATH", "xpath",f"//input[@*='Search patients'][@type='search']",1,"patient Name text field",driver)
                                from droid_activities import emptyelement
                                emptyelement.type_element("By.XPATH","xpath",f"//input[@*='Search patients'][@type='search']",1,driver,"Patient Name Text Field")
                                import time
                                time.sleep(1)
                                from droid_activities import TypeElement
                                TypeElement.type_element("By.XPATH", "xpath",f"//input[@*='Search patients'][@type='search']",Scheduled_Patients_PNO,1,driver,"Type Patient Name")
                                import time
                                time.sleep(2)
                                from droid_activities import ElementWait
                                Patient_notexist = ElementWait.element_wait(driver, "By.XPATH", f"//div[contains(@class,'text-p-gray600')]//div[contains(.,'No results, try searching')]",10)
                                if(Patient_notexist == True): # Patients not Available
                                    from droid_activities import excelappend
                                    excelappend.append_excel('C:\\RisePT\\Daily Summary Folder'+'\\'+'RisePT_PatientCoordination_SummaryReport - '+currentdate.replace('-','.')+'.xlsx', [currentdate,"N/A","Scheduled Patients",Fname+" "+Lname,DOB_Scheduled,"N/A","N/A",'Needs Attention','This patient not available, so skipped the patient'], 'Sheet1')
                                    Loop_Count=Loop_Count+1
                                    from droid_activities import windowhandle
                                    windowhandle.window_handle(driver,2)
                                    from droid_activities import ClickElement
                                    ClickElement.click_element("By.XPATH", "xpath",f"//button[.//span[normalize-space(.)='Close']]",1," Click Close",driver)
                                    time.sleep(3)
                                    continue
                                from droid_activities import ClickElement
                                ClickElement.click_element("By.XPATH", "xpath",f"//div[contains(@class, 'text-weight-medium') and contains(@class, 'text-subtitle1')]",1,"Patient Profile",driver)
                                import time
                                time.sleep(2)
                                from droid_activities import hoverElement
                                hoverElement.hover_element("By.XPATH", "xpath",f"//div[contains(@class,'q-chip')][.//div[normalize-space()='Visits']]",1,"Visits",driver)
                                from droid_activities import ClickElement
                                ClickElement.click_element("By.XPATH", "xpath",f"//div[contains(@class,'q-chip')][.//div[normalize-space()='Visits']]",1,"Visits Menu",driver)
                                time.sleep(3)
                                from droid_activities import GetTextElement 
                                Get_future= GetTextElement.get_textElement("By.XPATH",f"//div[normalize-space()='Future']/following-sibling::div[1]",1,"Get Future",driver)
                                print(Get_future)
                                Get_future=int(Get_future)
                                Get_All= GetTextElement.get_textElement("By.XPATH",f"//button[.//div[normalize-space()='All']]//div[contains(@class,'bg-p')]",1,"Get All",driver)
                                print(Get_All)
                                Get_All=int(Get_All)
                                from droid_activities import ElementWait
                                visit_missing = ElementWait.element_wait(driver, "By.XPATH", f"//i[@class='p-pa-xs q-icon text-p-red600 mdi mdi-alert-outline']",5)
                                from droid_activities import ElementWait
                                visit_Open_Exists = ElementWait.element_wait(driver, "By.XPATH", f"//div[@class='q-chip__content col row no-wrap items-center q-anchor--skipped']//div[contains(@class, 'text-p-gray700') and normalize-space(text())='Open']",5)
                                if(visit_Open_Exists == True or Get_All > 0 ): # Visits are Available so go to the solumn then rempve work flow
                                    from droid_activities import windowhandle
                                    windowhandle.window_handle(driver,2)
                                    time.sleep(3)
                                    from droid_activities import ClickElement
                                    ClickElement.click_element("By.XPATH", "xpath",f"(//button[@aria-haspopup='menu' and normalize-space()='Actions'])[2]",3,"Click Action",driver)
                                    ClickElement.click_element("By.XPATH", "xpath",f"//div[@role='menuitem' and contains(., 'Remove from Workflow')]",3,"Click Case not used",driver)
                                    from droid_activities import hoverElement
                                    hoverElement.hover_element("By.XPATH", "xpath",f"//div[contains(@class, 'inline-flex')]/h2[contains(text(), 'Scheduled Patients')]",1,"Scheduled Patients",driver)
                                    time.sleep(1)
                                    from droid_activities import ClickElement
                                    ClickElement.click_element("By.XPATH", "xpath",f"//div[contains(@class, 'inline-flex')]/h2[contains(text(), 'Scheduled Patients')]",1," Click Scheduled Patients",driver)
                                    time.sleep(1)
                                    from droid_activities import excelappend
                                    excelappend.append_excel('C:\\RisePT\\Daily Summary Folder'+'\\'+'RisePT_PatientCoordination_SummaryReport - '+currentdate.replace('-','.')+'.xlsx', [currentdate,"N/A","Scheduled Patients",Fname+" "+Lname,DOB_Scheduled,"N/A","N/A",'Success','This patient has been removed from the workflow'], 'Sheet1')
                                    Loop_Count=Loop_Count+1
                                elif (visit_missing == True):
                                    # from droid_activities import ClickElement
                                    # ClickElement.click_element("By.XPATH", "xpath",f"(//button[.//i[contains(@class,'mdi-checkbox-marked-circle-plus-outline')]])[2]",4,"Click Task Button",driver)
                                    time.sleep(2)
                                    from droid_activities import windowhandle
                                    windowhandle.window_handle(driver,2)
                                    from droid_activities import ClickElement
                                    ClickElement.click_element("By.XPATH", "xpath",f"//button[.//span[normalize-space(.)='Close']]",1," Click Close",driver)
                                    from droid_activities import excelappend
                                    excelappend.append_excel('C:\\RisePT\\Daily Summary Folder'+'\\'+'RisePT_PatientCoordination_SummaryReport - '+currentdate.replace('-','.')+'.xlsx', [currentdate,"N/A","Scheduled Patients",Fname+" "+Lname,DOB_Scheduled,"N/A","N/A",'Needs Attention','The patient visits are not available, so skipped the patient'], 'Sheet1')
                                    Loop_Count=Loop_Count+1
                                else:
                                    from droid_activities import ClickElement
                                    #ClickElement.click_element("By.XPATH", "xpath",f"(//button[.//i[contains(@class,'mdi-checkbox-marked-circle-plus-outline')]])[2]",4,"Click Task Button",driver)
                                    time.sleep(2)
                                    from droid_activities import windowhandle
                                    windowhandle.window_handle(driver,2)
                                    from droid_activities import ClickElement
                                    ClickElement.click_element("By.XPATH", "xpath",f"//button[.//span[normalize-space(.)='Close']]",1," Click Close",driver)
                                    from droid_activities import excelappend
                                    excelappend.append_excel('C:\\RisePT\\Daily Summary Folder'+'\\'+'RisePT_PatientCoordination_SummaryReport - '+currentdate.replace('-','.')+'.xlsx', [currentdate,"N/A","Scheduled Patients",Fname+" "+Lname,DOB_Scheduled,"N/A","N/A",'Needs Attention','The patient visits are not available, so skipped the patient'], 'Sheet1')
                                    Loop_Count=Loop_Count+1
                            else: #Else Start - Out Going Call Invalid
                                import time
                                time.sleep(3)
                                from droid_activities import message_box_delay
                                message_box_delay.show_timed_message_box('No Launch Page Exist -PatientHeader', 1)
                                ClickElement.click_element("By.XPATH", "xpath",f"//button[.//span[normalize-space(.)='Close']]",1," Click Close",driver)
                                from droid_activities import excelappend
                                excelappend.append_excel('C:\\RisePT\\Daily Summary Folder'+'\\'+'RisePT_PatientCoordination_SummaryReport - '+currentdate.replace('-','.')+'.xlsx', [currentdate,"N/A","Scheduled Patients",Fname+" "+Lname,DOB_Scheduled,"N/A","N/A",'Needs Attention','The patient visits are not available, so skipped the patient'], 'Sheet1')
                                Loop_Count=Loop_Count+1
                        else: #else for While loop break condition for Follow Up call column
                            print("All the Valid Follow Up patients are Completed")
                            break
                except:
                    print("Schedule Patients Except Part")
                    import traceback
                    Er = traceback.format_exc()
                    print(f"An error occurred: {Er}") 
                    time.sleep(2)
                    
                #<-------------- Schedule Patients End ------------------------------>
                
                #<-------------- Lost Discharge step Started ------------------------>
                try:
                    time.sleep(5)
                    windowhandle.window_handle(driver,2)
                    time.sleep(5)
                    from droid_activities import date_time
                    currentdate = date_time.date_time('%m-%d-%Y', 'current',0, "currentdate","currentdate")
                    from droid_activities import hoverElement
                    hoverElement.hover_element("By.XPATH", "xpath",f"//div[@class='flex items-center justify-between mb-4']//h2[contains(., 'Lost- Discharge')]",1,"Lost- Discharge",driver)
                    time.sleep(1)
                    from droid_activities import ClickElement
                    #ClickElement.click_element("By.XPATH", "xpath",f"(//h2[contains(@title,'Lost- Discharge Patient')]  /ancestor::div[contains(@class,'h-full') and contains(@class,'p-4')]  //div[@role='button' and @data-sentry-component='SortableItem'])[1]",5," Click Lost- Discharge Patient ",driver)
                    time.sleep(1)
                    from droid_activities import GetTextElement
                    Discharge_Count = GetTextElement.get_textElement("By.XPATH",f"//h2[contains(normalize-space(),'Lost- Discharge')] /parent::div /parent::div /following-sibling::div[1]",1,"Get Lost- Discharge Count",driver)
                    print(Discharge_Count)
                    Lastdischarge_phoneNo =[]
                    Discharge_Count=int(Discharge_Count)
                    Count_Loop=1
                    count_increment=1
                    while(True):
                        if(Discharge_Count>=Count_Loop):
                            print("Count_Loop : "+ str(Count_Loop))
                            while(True):
                                try:
                                    print("count_increment: "+ str(count_increment))
                                    from droid_activities import hoverElement
                                    hoverElement.hover_element("By.XPATH", "xpath",f"(//h2[@title='Lost- Discharge Patient']  /ancestor::div[@data-stage-id]  //div[@role='button' and @aria-roledescription='draggable'] )[{count_increment}]",1,"Lost- Discharge Patient",driver)
                                    time.sleep(3)
                                    from droid_activities import hoverElement
                                    hoverElement.hover_element("By.XPATH", "xpath",f"(//h2[@title='Lost- Discharge Patient']  /ancestor::div[@data-stage-id]  //div[@role='button' and @aria-roledescription='draggable'] )[{count_increment}]",1,"Lost- Discharge Patient",driver)
                                    time.sleep(5)
                                    from droid_activities import ClickElement
                                    ClickElement.click_element("By.XPATH", "xpath",f"(//h2[@title='Lost- Discharge Patient']  /ancestor::div[@data-stage-id]  //div[@role='button' and @aria-roledescription='draggable'] )[{count_increment}]",5," Click Lost- Discharge Patients",driver)
                                    time.sleep(5)
                                    break
                                except:
                                    from droid_activities import hoverElement
                                    hoverElement.hover_element("By.XPATH", "xpath",f"//h2[@title='Lost- Discharge Patient']/ancestor::div[@data-stage-id]//button[starts-with(.,'Load More')]",5,"Load more for Lost- Discharge Patient",driver)
                                   

                                    import pyautogui
                                    import time

                                    time.sleep(5)

                                    for _ in range(20):
                                        pyautogui.press('end')
                                        time.sleep(0.1)
                                    import time
                                    time.sleep(2)
                                    from droid_activities import hoverElement
                                    hoverElement.hover_element("By.XPATH", "xpath",f"//h2[@title='Lost- Discharge Patient']/ancestor::div[@data-stage-id]//button[starts-with(.,'Load More')]",5,"Load more for Lost- Discharge Patient",driver)
                                    time.sleep(5)
                                    ClickElement.click_element("By.XPATH", "xpath",f"//h2[@title='Lost- Discharge Patient']/ancestor::div[@data-stage-id]//button[starts-with(.,'Load More')]",5,"Lost- Discharge Patient  Click Load More Button",driver)# need to add click extra patient step
                                    time.sleep(2)
                                    print("click extra patinents") # need to add click extra patient step
                            while(True):
                                from droid_activities import ElementWait
                                PatientDetails_exist = ElementWait.element_wait(driver, "By.XPATH", f"//button[@role='tab' and normalize-space()='Patient Details']",10)
                                if(PatientDetails_exist == True):
                                    break
                                else:
                                    time.sleep(5)
                            from droid_activities import GetTextElement
                            LastDischrge_Patient_PNO = GetTextElement.get_textElement("By.XPATH",f"//div[contains(@aria-label, 'Phone Number')]",1,"Get Phone Number",driver)
                            if (Count_Loop >= 2):
                                if LastDischrge_Patient_PNO in Lastdischarge_phoneNo:
                                    count_increment = count_increment+1
                                    time.sleep(5)
                                    ClickElement.click_element("By.XPATH", "xpath",f"//button[.//span[normalize-space(.)='Close']]",1," Click Close",driver)
                                    continue
                            Lastdischarge_phoneNo.append(LastDischrge_Patient_PNO)
                            Last_Fname = GetTextElement.get_textElement("By.XPATH",f"//div[@role='button'][contains(@aria-label, 'First Name')]",1,"First Name",driver)
                            print(Last_Fname)
                            from droid_activities import GetTextElement
                            Last_Lname = GetTextElement.get_textElement("By.XPATH",f"//div[@role='button'][contains(@aria-label, 'Last Name')]",1,"Last Name",driver)
                            print(Last_Lname)
                            from droid_activities import GetTextElement
                            Last_DOB_4th = GetTextElement.get_textElement("By.XPATH",f"//div[@role='button'][contains(@aria-label, 'Date of Birth')]",1,"Get DOB",driver)
                            print(Last_DOB_4th)
                            PatientDetails_exist=False
                            from droid_activities import ElementWait
                            PatientDetails_exist = ElementWait.element_wait(driver, "By.XPATH", f"//button[@role='tab' and normalize-space()='Patient Details']",10)
                            launchcount = int(0) #int
                            if PatientDetails_exist == True: #range
                                print("inside Patients Details")
                                from droid_activities import message_box_delay
                                message_box_delay.show_timed_message_box('Launch Page Exist - PatientHeader', 1)
                                from droid_activities import hoverElement
                                hoverElement.hover_element("By.XPATH", "xpath",f"//*[@role='button' and contains(@aria-label,'Comments')]",1,"Hover additional-information",driver)
                                try:
                                    from selenium.webdriver.common.by import By
                                    from selenium.webdriver.support.ui import WebDriverWait
                                    from selenium.webdriver.support import expected_conditions as EC
                                    wait = WebDriverWait(driver, 10)
                                    element = wait.until(EC.presence_of_element_located((By.XPATH, "//*[@role='button' and contains(@aria-label,'Comments')]")))
                                    Cmd_Date = element.text
                                    print(Cmd_Date)
                                except:
                                    print(" Get Comment Field")
                                try:
                                    import re
                                    from datetime import datetime
                                    # Cmd_Date = "DC if not scheduled by 6/8/2026"
                                    match = re.search(r"\d{1,2}/\d{1,2}/\d{2,4}", Cmd_Date)
                                    if match:
                                        date_str = match.group()
                                        try:
                                            date_obj = datetime.strptime(date_str, "%m/%d/%Y")
                                        except ValueError:
                                            date_obj = datetime.strptime(date_str, "%m/%d/%y")
                                        print(date_obj.date())  # 2026-06-08
                                    else:
                                        from datetime import datetime, timedelta
                                        date_str = (datetime.now() - timedelta(days=1)).strftime("%m/%d/%y")
                                        date_obj = datetime.strptime(date_str, "%m/%d/%y")
                                        # ClickElement.click_element("By.XPATH", "xpath",f"//button[.//span[normalize-space(.)='Close']]",1," Click Close",driver)
                                        # from droid_activities import excelappend
                                        # excelappend.append_excel('C:\\RisePT\\Daily Summary Folder'+'\\'+'RisePT_PatientCoordination_SummaryReport - '+currentdate.replace('-','.')+'.xlsx', [currentdate,"N/A","Discharge",Last_Fname+" "+Last_Lname,Last_DOB_4th,"N/A","N/A",'Needs Attention','Discharge Date Not Available'], 'Sheet1')
                                        # Count_Loop=Count_Loop+1 
                                        # continue
                                except:
                                    print("Date are Not Available")
                                    from datetime import datetime, timedelta
                                    yesterday = datetime.now() - timedelta(days=5)
                                    date_obj_str = yesterday.strftime("%m/%d/%y")
                                    date_obj = datetime.strptime(date_obj_str, "%m/%d/%y") 
                                    print(date_obj)                                  
                                from droid_activities import date_time
                                currentdate = date_time.date_time('%m/%d/%Y', 'current',0, "currentdate","currentdate")
                                date_Current = datetime.strptime(currentdate, "%m/%d/%Y")
                                print(date_Current)
                                if(date_Current >= date_obj):
                                    print("if condition")
                                    import time
                                    time.sleep(5)
                                    from droid_activities import openbrowser
                                    from droid_activities import windowhandle
                                    switch_to_window_by_title(driver, "prompt")
                                    from droid_activities import ClickElement
                                    ClickElement.click_element("By.XPATH", "xpath",f"//a[.//div[normalize-space()='Patients']]",1,"Patients Menu",driver)
                                    from droid_activities import hoverElement
                                    hoverElement.hover_element("By.XPATH", "xpath",f"//input[@*='Search patients'][@type='search']",1,"Patient Name Text Field",driver)
                                    time.sleep(1)
                                    from droid_activities import ClickElement
                                    ClickElement.click_element("By.XPATH", "xpath",f"//input[@*='Search patients'][@type='search']",1,"patient Name text field",driver)
                                    from droid_activities import emptyelement
                                    emptyelement.type_element("By.XPATH","xpath",f"//input[@*='Search patients'][@type='search']",1,driver,"Patient Name Text Field")
                                    import time
                                    time.sleep(1)
                                    from droid_activities import TypeElement
                                    TypeElement.type_element("By.XPATH", "xpath",f"//input[@*='Search patients'][@type='search']",LastDischrge_Patient_PNO,1,driver,"Type Patient Name")
                                    import time
                                    time.sleep(2)
                                    from droid_activities import ElementWait
                                    Patient_notexist = ElementWait.element_wait(driver, "By.XPATH", f"//div[contains(@class,'text-p-gray600')]//div[contains(.,'No results, try searching')]",10)
                                    if(Patient_notexist == True):
                                        print("Patient Not found")
                                        from droid_activities import ClickElement
                                        ClickElement.click_element("By.XPATH", "xpath",f"//a[.//div[normalize-space()='Patients']]",1,"Patients Menu",driver)
                                        from droid_activities import hoverElement
                                        hoverElement.hover_element("By.XPATH", "xpath",f"//input[@*='Search patients'][@type='search']",1,"Patient Name Text Field",driver)
                                        time.sleep(1)
                                        from droid_activities import ClickElement
                                        ClickElement.click_element("By.XPATH", "xpath",f"//input[@*='Search patients'][@type='search']",1,"patient Name text field",driver)
                                        from droid_activities import emptyelement
                                        emptyelement.type_element("By.XPATH","xpath",f"//input[@*='Search patients'][@type='search']",1,driver,"Patient Name Text Field")
                                        import time
                                        time.sleep(1)
                                        from droid_activities import TypeElement
                                        TypeElement.type_element("By.XPATH", "xpath",f"//input[@*='Search patients'][@type='search']",Last_Fname+" "+Last_Lname,1,driver,"Type Patient Name")
                                        from droid_activities import ElementWait
                                        Patient_notexist = ElementWait.element_wait(driver, "By.XPATH", f"//div[contains(@class,'text-p-gray600')]//div[contains(.,'No results, try searching')]",10)
                                        if(Patient_notexist):
                                            print("patient not Found")
                                            time.sleep(2)
                                            from droid_activities import windowhandle
                                            windowhandle.window_handle(driver,2)
                                            time.sleep(3)
                                            from droid_activities import date_time
                                            currentdate = date_time.date_time('%m-%d-%Y', 'current',0, "currentdate","currentdate")
                                            from droid_activities import ClickElement
                                            ClickElement.click_element("By.XPATH", "xpath",f"(//button[@aria-haspopup='menu' and normalize-space()='Actions'])[2]",3,"Click Action",driver)
                                            ClickElement.click_element("By.XPATH", "xpath",f"//div[@role='menuitem' and contains(., 'Remove from Workflow')]",3,"Click Case not used",driver)
                                            from droid_activities import excelappend
                                            excelappend.append_excel('C:\\RisePT\\Daily Summary Folder'+'\\'+'RisePT_PatientCoordination_SummaryReport - '+currentdate.replace('-','.')+'.xlsx', [currentdate,"N/A","Discharge",Last_Fname+" "+Last_Lname,Last_DOB_4th,"N/A","N/A",'Needs Attention','The patient not found in prompt portal'], 'Sheet1')
                                            continue
                                        else:#Patient found
                                            print("Patient Found")
                                    from droid_activities import ClickElement
                                    ClickElement.click_element("By.XPATH", "xpath",f"(//div[contains(@class,'patient')])[1]",1,"Patient Profile",driver)
                                    import time
                                    time.sleep(3)
                                    from droid_activities import GetTextElement 
                                    Lastname= GetTextElement.get_textElement("By.XPATH",f"//div[normalize-space()='Date of Birth']/following::span[1]",1,"Get Last Name",driver)
                                    print(Lastname)
                                    Account_name = GetTextElement.get_textElement("By.XPATH",f"//div[normalize-space()='Account Number']/following::span[1]",1,"Get Account Number",driver)
                                    print(Account_name)
                                    from droid_activities import ClickElement
                                    ClickElement.click_element("By.XPATH", "xpath",f"//div[text()='Visits']",1,"Visits Menu",driver)
                                    Get_All= GetTextElement.get_textElement("By.XPATH",f"//button[.//div[normalize-space()='All']]//div[contains(@class,'bg-p')]",1,"Get All",driver)
                                    print(Get_All)
                                    Get_All=int(Get_All)
                                    from droid_activities import GetTextElement 
                                    Get_future= GetTextElement.get_textElement("By.XPATH",f"//div[normalize-space(text())='Future']/following-sibling::div[normalize-space()]",1,"Get Future",driver)
                                    print(Get_future)
                                    Get_future=int(Get_future)
                                    from droid_activities import ElementWait
                                    NotCheckedIn_Exists = ElementWait.element_wait(driver, "By.XPATH", f"//tr[.//div[contains(text(),'Not Checked In')]]",10)
                                    from droid_activities import ElementWait
                                    is_visit_missing = ElementWait.element_wait(driver, "By.XPATH", f"//i[@class='p-pa-xs q-icon text-p-red600 mdi mdi-alert-outline']",10)
                                    from droid_activities import ElementWait
                                    visit_missing = ElementWait.element_wait(driver, "By.XPATH", f"//i[@class='p-pa-xs q-icon text-p-red600 mdi mdi-alert-outline']",5)
                                    from droid_activities import ElementWait
                                    visit_Open_Exists = ElementWait.element_wait(driver, "By.XPATH", f"//div[@class='q-chip__content col row no-wrap items-center q-anchor--skipped']//div[contains(@class, 'text-p-gray700') and normalize-space(text())='Open']",5)
                                    # if(Get_All >= 0 or is_visit_missing == True ):
                                    if(Get_future <= 0 or NotCheckedIn_Exists == False):
                                        from droid_activities import ClickElement
                                        ClickElement.click_element("By.XPATH", "xpath",f"//div[text()='Cases']",1,"Cases Menu",driver)
                                        from droid_activities import ElementWait
                                        is_Discharged = ElementWait.element_wait(driver, "By.XPATH", f"//button[.//span[normalize-space()='Discharge Case']]",10)
                                        if(is_Discharged != True):
                                            print(" This Patients already Discharged")
                                            time.sleep(2)
                                            from droid_activities import windowhandle
                                            windowhandle.window_handle(driver,2)
                                            time.sleep(3)
                                            from droid_activities import date_time
                                            currentdate = date_time.date_time('%m-%d-%Y', 'current',0, "currentdate","currentdate")
                                            from droid_activities import ClickElement
                                            ClickElement.click_element("By.XPATH", "xpath",f"(//button[@aria-haspopup='menu' and normalize-space()='Actions'])[2]",3,"Click Action",driver)
                                            ClickElement.click_element("By.XPATH", "xpath",f"//div[@role='menuitem' and contains(., 'Remove from Workflow')]",3,"Click Case not used",driver)
                                            from droid_activities import excelappend
                                            excelappend.append_excel('C:\\RisePT\\Daily Summary Folder'+'\\'+'RisePT_PatientCoordination_SummaryReport - '+currentdate.replace('-','.')+'.xlsx', [currentdate,"N/A","Discharge",Last_Fname+" "+Last_Lname,Last_DOB_4th,"N/A","N/A",'Success','The patients workflow has been successfully processed'], 'Sheet1')
                                            continue  
                                        else:
                                            print(" Its Not Already Discharged ") 
                                        Get_Referring_Provider=""
                                        try:
                                            hoverElement.hover_element("By.XPATH", "xpath",f"//div[normalize-space(text())='Referring Provider (PRIMARY)'][1]",1,"Referring Provider (PRIMARY)",driver)
                                            from droid_activities import GetTextElement 
                                            Get_Referring_Provider= GetTextElement.get_textElement("By.XPATH",f"//div[normalize-space(text())='Referring Provider (PRIMARY)']/following::span[@class='text-p-gray600'][1]",1,"Get Referring_Provider",driver)
                                            print(Get_Referring_Provider)
                                            parts = [p.strip() for p in Get_Referring_Provider.split(",")]
                                            if len(parts) == 2:
                                                last, first = parts
                                                Referring_Provider = f"{first} {last}"
                                            elif len(parts) == 3:
                                                last, md, first = parts
                                                Referring_Provider = f"{first} {last}"
                                            print(Referring_Provider)
                                            time.sleep(3)
                                        except:
                                            print(" Not Found Referring Provider ")
                                        if (Get_Referring_Provider != ""):
                                            try:
                                                from droid_activities import hoverElement
                                                hoverElement.hover_element("By.XPATH", "xpath",f"//div[@class='ellipsis' and normalize-space(.)='Files']",1,"Files Menu",driver)
                                                from droid_activities import ClickElement
                                                ClickElement.click_element("By.XPATH", "xpath",f"//div[@class='ellipsis' and normalize-space(.)='Files']",1,"Files Menu",driver)
                                                import time
                                                time.sleep(1)
                                                ClickElement.click_element("By.XPATH", "xpath",f"//a[normalize-space(text())='All Files']",7,"Click All Files",driver)
                                                time.sleep(3)
                                                try:
                                                    from droid_activities import hoverElement
                                                    hoverElement.hover_element("By.XPATH", "xpath",f"//div[contains(@class, 'q-expansion-item')] [.//div[contains(normalize-space(.), 'Referral')]] //button[.//i[text()='more_vert']]",1,"Referral Menu",driver)
                                                    ClickElement.click_element("By.XPATH", "xpath",f"//div[contains(@class, 'q-expansion-item')] [.//div[contains(normalize-space(.), 'Referral')]] //button[.//i[text()='more_vert']]",7,"Click Referral",driver)
                                                except:
                                                    try:
                                                        from droid_activities import hoverElement
                                                        hoverElement.hover_element("By.XPATH", "xpath",f"//div[contains(@class, 'q-expansion-item')] [.//div[contains(normalize-space(.), 'REF')]] //button[.//i[text()='more_vert']]",1,"Referral Menu",driver)
                                                        ClickElement.click_element("By.XPATH", "xpath",f"//div[contains(@class, 'q-expansion-item')] [.//div[contains(normalize-space(.), 'REF')]] //button[.//i[text()='more_vert']]",7,"Click Referral",driver)
                                                    except:
                                                        try:
                                                            from droid_activities import hoverElement
                                                            hoverElement.hover_element("By.XPATH", "xpath",f"//div[contains(@class, 'q-expansion-item')] [.//div[contains(normalize-space(.), 'ref')]] //button[.//i[text()='more_vert']]",1,"Referral Menu",driver)
                                                            ClickElement.click_element("By.XPATH", "xpath",f"//div[contains(@class, 'q-expansion-item')] [.//div[contains(normalize-space(.), 'ref')]] //button[.//i[text()='more_vert']]",7,"Click Referral",driver)
                                                        except:
                                                            from droid_activities import hoverElement
                                                            hoverElement.hover_element("By.XPATH", "xpath",f"//div[contains(@class, 'q-expansion-item')] [.//div[contains(normalize-space(.), 'Doctor Referrel')]] //button[.//i[text()='more_vert']]",1,"Referral Menu",driver)
                                                            ClickElement.click_element("By.XPATH", "xpath",f"//div[contains(@class, 'q-expansion-item')] [.//div[contains(normalize-space(.), 'Doctor Referrel')]] //button[.//i[text()='more_vert']]",7,"Click Referral",driver)
                                                ClickElement.click_element("By.XPATH", "xpath",f"//button[.//span[normalize-space(text())='Fax']]",7,"Click Fax",driver)
                                                ClickElement.click_element("By.XPATH", "xpath",f"//div[contains(@class, 'q-field__control')] //div[normalize-space(text())='From Facility']/ancestor::div[contains(@class, 'q-field__control')]",7,"Click West Selected",driver)
                                                ClickElement.click_element("By.XPATH", "xpath",f"//div[@role='option']//div[normalize-space()='West']",7,"Click West",driver) 
                                                from droid_activities import ClickElement
                                                ClickElement.click_element("By.XPATH", "xpath",f"//label[.//div[contains(text(),'To Number')]]//i[text()='arrow_drop_down']",2,"Cick DropDown",driver)
                                                try:
                                                    from droid_activities import ClickElement
                                                    ClickElement.click_element("By.XPATH", "xpath",f"//div[contains(@class,'p-select__option-descriptor_gray') and contains(., '{Referring_Provider}')]",3,"Cick DropDown",driver)
                                                    time.sleep(3)
                                                    ClickElement.click_element("By.XPATH", "xpath",f"//textarea[@aria-label='Message']",7,"Click message",driver)
                                                    Temp_message = """We received a referral to schedule this patient for an evaluation and made four attempts
                                                    to contact them, but didn’t get a response. I'm sending the referral back to your office for now.
                                                    If the patient reaches out to us, we’re happy to get them scheduled.
                                                    If you have any questions, feel free to call us at 479-318-0017. Thank you!"""
                                                    print(Temp_message) # Check Message
                                                    import re
                                                    clean_message = re.sub(r"\s+", " ", Temp_message).strip()
                                                    from droid_activities import TypeElement
                                                    TypeElement.type_element("By.XPATH", "xpath",f"//textarea[@aria-label='Message']",clean_message,1,driver,"Type template Text")
                                                    time.sleep(3)
                                                    ClickElement.click_element("By.XPATH", "xpath",f"//button[.//span[normalize-space(text())='Send Fax']]",7,"Click Send Fax",driver)
                                                except:
                                                    from droid_activities import ClickCoordinate
                                                    ClickCoordinate.click_coordinates(1814,535,"Click")
                                                    from droid_activities import ClickCoordinate
                                                    ClickCoordinate.click_coordinates(1814,535,"Click")
                                                    print(" refering provider not available")
                                            except:
                                                print(" Files not found")
                                        from droid_activities import hoverElement
                                        hoverElement.hover_element("By.XPATH", "xpath",f"//div[text()='Cases']",3,"Case Menu",driver)
                                        ClickElement.click_element("By.XPATH", "xpath",f"//div[text()='Cases']",3,"Click Case",driver)
                                        ClickElement.click_element("By.XPATH", "xpath",f"//button[.//span[normalize-space(text())='Discharge Case']]",3,"Click Discharge Case",driver)
                                        ClickElement.click_element("By.XPATH", "xpath",f"//input[@aria-label='Discharge Date']",7,"Click Discharge Date",driver)
                                        from droid_activities import date_time
                                        Discharge_Date = date_time.date_time('%m/%d/%Y', 'current',0, "currentdate","currentdate")
                                        print(Discharge_Date)
                                        from droid_activities import TypeElement
                                        TypeElement.type_element("By.XPATH", "xpath",f"//input[@aria-label='Discharge Date']",Discharge_Date,3,driver,"Type Discharge Date")
                                        time.sleep(2)
                                        try:
                                            while(True):
                                                ClickElement.click_element("By.XPATH", "xpath",f"//div[normalize-space()='Discharge Reason']/ancestor::div[contains(@class,'q-field__control')]//i[contains(@class,'q-select__dropdown-icon')]",3,"Click Discharge Reason",driver)
                                                time.sleep(2)
                                                from droid_activities import ElementWait
                                                CasenotUsed_Exists = ElementWait.element_wait(driver,"By.XPATH",f"//div[@role='option' and normalize-space()='Case not used']",5)
                                                if(CasenotUsed_Exists):
                                                    ClickElement.click_element("By.XPATH", "xpath",f"//div[@role='option' and normalize-space()='Case not used']",3,"Click Case not used",driver)
                                                    from droid_activities import ElementWait
                                                    SelectedCasenotUsed_Exists= ElementWait.element_wait(driver,"By.XPATH",f"//input[@aria-label='Discharge Reason' and @value='Case not used']",3)
                                                    if(SelectedCasenotUsed_Exists):
                                                        ClickElement.click_element("By.XPATH", "xpath",f"//div[contains(@class,'q-ml-md') and .//span[normalize-space()='Discharge Case']][1]",3,"Click Discharge Case",driver)
                                                        break
                                        except:
                                            try:
                                                print("Case not used are exception")
                                                ClickElement.click_element("By.XPATH", "xpath",f"//div[normalize-space()='Discharge Reason'] /ancestor::label //input[@role='combobox']",3,"Click Discharge Reason",driver)
                                                time.sleep(2)
                                                ClickElement.click_element("By.XPATH", "xpath",f"//div[@role='option' and normalize-space()='Case not used']",3,"Click Case not used",driver)
                                                time.sleep(3)
                                                ClickElement.click_element("By.XPATH", "xpath",f"//div[contains(@class,'q-ml-md') and .//span[normalize-space()='Discharge Case']][1]",3,"Click Discharge Case",driver)
                                            except:
                                                from droid_activities import excelappend
                                                excelappend.append_excel('C:\\RisePT\\Daily Summary Folder'+'\\'+'RisePT_PatientCoordination_SummaryReport - '+currentdate.replace('-','.')+'.xlsx', [currentdate,"N/A","Discharge",Last_Fname+" "+Last_Lname,Last_DOB_4th,"N/A","N/A",'Needs Attention','Case not used Exception Occurs'], 'Sheet1')
                                                continue
                                        time.sleep(2)
                                        from droid_activities import windowhandle
                                        windowhandle.window_handle(driver,2)
                                        time.sleep(3)
                                        from droid_activities import date_time
                                        currentdate = date_time.date_time('%m-%d-%Y', 'current',0, "currentdate","currentdate")
                                        from droid_activities import ClickElement
                                        ClickElement.click_element("By.XPATH", "xpath",f"(//button[@aria-haspopup='menu' and normalize-space()='Actions'])[2]",3,"Click Action",driver)
                                        ClickElement.click_element("By.XPATH", "xpath",f"//div[@role='menuitem' and contains(., 'Remove from Workflow')]",3,"Click Case not used",driver)
                                        from droid_activities import excelappend
                                        excelappend.append_excel('C:\\RisePT\\Daily Summary Folder'+'\\'+'RisePT_PatientCoordination_SummaryReport - '+currentdate.replace('-','.')+'.xlsx', [currentdate,"N/A","Discharge",Last_Fname+" "+Last_Lname,Last_DOB_4th,"N/A","N/A",'Success','The patients workflow has been successfully processed'], 'Sheet1')
                                    else: #visits available or not
                                        print("Future dates available")
                                        try:
                                            from droid_activities import windowhandle
                                            windowhandle.window_handle(driver,2)
                                            ClickElement.click_element("By.XPATH", "xpath",f"//button[.//span[normalize-space(.)='Close']]",1," Click Close",driver)
                                        except:
                                            print(" No need Close Button")
                                        time.sleep(3)
                                        try:
                                            from droid_activities import date_time
                                            currentdate = date_time.date_time('%m-%d-%Y', 'current',0, "currentdate","currentdate")
                                            from droid_activities import excelappend
                                            excelappend.append_excel('C:\\RisePT\\Daily Summary Folder'+'\\'+'RisePT_PatientCoordination_SummaryReport - '+currentdate.replace('-','.')+'.xlsx', [currentdate,"N/A","Discharge",Last_Fname+" "+Last_Lname,Last_DOB_4th,"N/A","N/A",'Needs Attention','Future appointments are available for this patient'], 'Sheet1')
                                        except:
                                            import traceback
                                            Er = traceback.format_exc()
                                            print(f"An error occurred: {Er}")
                                            time.sleep(2)
                                        Count_Loop=Count_Loop+1
                                        from droid_activities import windowhandle
                                        windowhandle.window_handle(driver,2)
                                else: # Discharge Date not Available 
                                    ClickElement.click_element("By.XPATH", "xpath",f"//button[.//span[normalize-space(.)='Close']]",1," Click Close",driver)
                                    message_box_delay.show_timed_message_box('Clicked on the manual Verify of cases and Completed this patient processing', 1)
                                    from droid_activities import date_time
                                    currentdate = date_time.date_time('%m-%d-%Y', 'current',0, "currentdate","currentdate")
                                    try:
                                        from droid_activities import excelappend
                                        excelappend.append_excel('C:\\RisePT\\Daily Summary Folder'+'\\'+'RisePT_PatientCoordination_SummaryReport - '+currentdate.replace('-','.')+'.xlsx', [currentdate,"N/A","Discharge",Last_Fname+" "+Last_Lname,Last_DOB_4th,"N/A","N/A",'Needs Attention','The Solum portal contains an upcoming date for this patient'], 'Sheet1')
                                    except:
                                        try:
                                            from droid_activities import excelappend
                                            excelappend.append_excel('C:\\RisePT\\Daily Summary Folder'+'\\'+'RisePT_PatientCoordination_SummaryReport - '+currentdate.replace('-','.')+'.xlsx', [currentdate,"N/A","Discharge",Last_Fname+" "+Last_Lname,Last_DOB_4th,"N/A","N/A",'Needs Attention','The Solum portal contains an upcoming date for this patient'], 'Sheet1')
                                        except:
                                            print(" Excel append Issue")
                                    import time
                                    time.sleep(3)
                                    Count_Loop=Count_Loop+1
                            else: #Patient Details Page Exists Else
                                print("else part Page Exists Else")
                        else: # Patients Count Completed
                            print("Break While loop for Last Discharge")
                            from droid_activities import date_time
                            currentdate = date_time.date_time('%m-%d-%Y', 'current',0, "currentdate","currentdate")
                            from droid_activities import send_mail
                            tomail = ["Manikandan.c@droidal.com"]
                            ccmail = ["Manikandan.c@droidal.com"]
                            send_mail.send_email('C:\\RisePT\\Daily Summary Folder'+'\\'+'RisePT_PatientCoordination_SummaryReport - '+currentdate.replace('-','.')+'.xlsx','risept@droidal.ai','kqf8vZzhkAPeiuvp8Y',tomail,ccmail,"Last Discharge completed ",'', "summaryfile", 'smtp.office365.com', 587)
                            outerretry=2
                            from droid_activities import windowhandle
                            time.sleep(5)
                            switch_to_window_by_title(driver, "prompt")
                            driver.quit()
                            break             
                except:
                    print("Discharge Except Part")
                    from droid_activities import date_time
                    currentdate = date_time.date_time('%m-%d-%Y', 'current',0, "currentdate","currentdate")
                    from droid_activities import send_mail
                    tomail = ["Manikandan.c@droidal.com"]
                    ccmail = ["Manikandan.c@droidal.com"]
                    send_mail.send_email('C:\\RisePT\\Daily Summary Folder'+'\\'+'RisePT_PatientCoordination_SummaryReport - '+currentdate.replace('-','.')+'.xlsx','risept@droidal.ai','kqf8vZzhkAPeiuvp8Y',tomail,ccmail," Patients coordination is completed",'', "summaryfile", 'smtp.office365.com', 587)
                    outerretry=2
                    import traceback
                    Er = traceback.format_exc()
                    print(f"An error occurred: {Er}") 
                    time.sleep(2)
                    from droid_activities import windowhandle
                    time.sleep(5)
                    switch_to_window_by_title(driver, "prompt")
                    driver.quit()
            #<--------------------- End Last Discharge Loop ------------------------------------------------------------->                                          
        except:
            import traceback
            Er = traceback.format_exc()
            print(f"An error occurred: {Er}")
            switch_to_window_by_title(driver, "prompt")
            outerretry=2
            driver.quit()
            from droid_activities import excelappend
            #excelappend.append_excel('C:\\RisePT\\Daily Summary Folder'+'\\'+'RisePT_PatientCoordination_SummaryReport - '+currentdate.replace('-','.')+'.xlsx', [currentdate,TaskID,Tasktitle,Patientname,"N/A",TaskAssingnee,Accountnumber,'Need Attention','The patients workflow not successfully processed'], 'Sheet1')
            time.sleep(2)
