I build this project to help people who want to monitor package shipped from US to China.
The function of this module are:
    1.let user define own contact based on wechat 
            a. initialize own contact with format:
                    real_name   wechat_remark_name  cell_number provience   city    district    details 
            b. module will load contact in system, once there is matched msg need to be sent, it will use this info 
                    tips: be sure wechat_remark_name is unique,otherwise system will send msg to yourself
    2. let user define input package info including 
            a. tracking number
            b. purchaser info by contact id 
            c. receiver info  by contact id
            d. content : current version not able to login supplier webpage to catch those data
            remind msg will mainly send to purchaser, inform receiver only if package arrive in destnation city      
    3. Wechat login interface 
            a. System will run check twice a day
            b. Once System detect update, will inform you by owner's wechat with msg " detected summary of updates "
            c. After receiving your reply to confirm login, a matrix code will send to you by wechat
            d. Besure use your cell camera to scan inorder to login your webwechat send out msg
            e. You wechat will be automatically logged out right after msgs are sentout done
            f. The catch will stored in server, means you don't need to login by scan code every time
    4. Period report :
            a. the system will create period report based on your setting, the default is monthly for user
            b. report will including :
                    total package placed 
                    total packagd delivered
                    top 10 purchasers 
                    top 10 best sell products
                    top 10 cities in a map
            c. annual report 
     
