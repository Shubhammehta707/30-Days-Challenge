""" Login Security with Multiple Conditions
Build a login verification program.
Rules:
1. Username must be correct.
2. Password must be correct.
3. Account must be active.
4. OTP must be correct.
5. After three failed login attempts, lock the account.
Tricky condition: The username and password are correct, but the account is inactive and the OTP is also incorrect.
Task: Use nested conditions and logical operators to identify the exact failure reason. The program should stop authentication as soon as a required check fails."""

CORRECT_USERNAME = "admin"
CORRECT_PASSWORD = "password123"
IS_ACCOUNT_ACTIVE = False
CORRECT_OTP = "123456"

failed_attempts = 0

user_in = input("Entet your username: ")
pass_in = input("Enter your password: ")
otp_in = input("Enter your otp: ")

print("--- Starting Login Verification ---")

if failed_attempts >= 3:
    print("Authentication Failed: Account is locked due to too many failed attempts.")
else:
    if user_in == CORRECT_USERNAME:
        if pass_in == CORRECT_PASSWORD:
            if IS_ACCOUNT_ACTIVE:
                if otp_in == CORRECT_OTP:
                    print("Authentication Successful: Welcome!")
                    failed_attempts = 0
                else:
                    failed_attempts = failed_attempts + 1
                    print("Authentication Failed: OTP is incorrect.")
                    if failed_attempts >= 3:
                        print("Notice: Account has been locked.")
            else:
                print("Authentication Failed: Account is inactive.")
        else:
            failed_attempts = failed_attempts + 1
            print("Authentication Failed: Password is incorrect.")
            if failed_attempts >= 3:
                print("Notice: Account has been locked.")
    else:
        failed_attempts = failed_attempts + 1
        print("Authentication Failed: Username is incorrect.")
        if failed_attempts >= 3:
            print("Notice: Account has been locked.")
