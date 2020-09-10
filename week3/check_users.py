def check_users(current_users, new_users):
    pass
    for new_user in new_users:
        for current_user in current_users:
            if new_user.lower() == current_user.lower():
                print(f"The username: {new_user} is already taken")
        if new_user.lower() != current_user.lower():
            print(f"The username: {new_user} is available")        
          
if __name__ == "__main__":
    current_users = ['chris','haritha','sally','darnell','superman']
    new_users = ['george','ringo','superman','hannibal']
    check_users(current_users, new_users)