import praw

def redditComment(subreddit_name,total_iterations,N):
    reddit = praw.Reddit(client_id='<your-reddit-client-id>', 
            client_secret='<your-reddit-secret-key>', 
            user_agent='<your-reddit-project-name>')
    hot_subreddit = reddit.subreddit(subreddit_name).hot(limit=N)
    
    authors=[]
    comments=[]   
    for post in hot_subreddit:
        post = post
    for i in range(total_iterations):
        if len(post.comments[i].body)<1000:
            authors.append(post.comments[i].author)
            comments.append(post.comments[i].body)
    total_iterations = len(authors)
    return (post,authors,comments, total_iterations)
    
    