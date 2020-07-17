def groups_per_user(group_dictionary):

    user_groups = {}
    # Go through group_dictionary
    for group in group_dictionary:
        for user in group_dictionary[group]:
            if user in user_groups.keys():
              user_groups[user] = (user_groups[user]).append(group)
            else:
                user_groups[user]=[group];
                print(user_groups[user])

    # Now add the group to the the list of
    # groups for this user, creating the entry
    # in the dictionary if necessar
    return (user_groups)


print(groups_per_user({"local": ["admin", "userA"],
                       "public": ["admin", "userB"],
                       "administrator": ["admin"]}))