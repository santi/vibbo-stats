def print_metrics(messages):
    # print the total number of messages
    print(f"Total number of messages: {len(messages)}")

    # Group the messages by createdBy.name and count the number of messages for each user:
    message_count = {}
    for message in messages:
        name = message["createdBy"]["name"]
        if name not in message_count:
            message_count[name] = 0
        message_count[name] += 1

    # print top 10 most active users and print them as "Name: Count"
    print("Top 10 most active users by number of send messages:")
    top_10 = sorted(message_count.items(), key=lambda x: x[1], reverse=True)[:10]
    for name, count in top_10:
        print(f"{name}: {count}")

    # Count the number of words each user has written in total:
    word_count = {}
    for message in messages:
        name = message["createdBy"]["name"]
        if name not in word_count:
            word_count[name] = 0
        word_count[name] += len(message["body"].split())
        
    # print top 10 most active users and print them as "Name: Count"
    print("Top 10 most active users by number of written words:")
    top_10 = sorted(word_count.items(), key=lambda x: x[1], reverse=True)[:10]
    for name, count in top_10:
        print(f"{name}: {count}")
    