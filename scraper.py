from bs4 import BeautifulSoup
import requests
import time
import sys

FORUM_PAGE_ROOT = "https://www.vlr.gg/threads/?sort=top&page="
THREAD_ROOT = "https://www.vlr.gg"
USER_ROOT = "https://www.vlr.gg/user/"

def get_user_posts(samples):
    process_start = time.time()

    users = set()
    post_links = set()

    print("Getting pages...", end = "\r")
    for i in range(samples):
        page_num = str(i)
        link = FORUM_PAGE_ROOT + page_num
        #print("PAGE : ", link)
        # print("Acessing ", link)
        soup = BeautifulSoup(requests.get(link).content, features = 'lxml')
        #print("GOT SOUP FOR PAGE")

        post_links = post_links.union(get_posts_from_page(soup))
    
    # print(post_links)
    print("Getting users...", end = "\r")
    for link in post_links:
        users = users.union(get_user_names_from_link(link))
    
    # print(users) 

    user_posts = {}
    total = len(users)
    completed = 0
    print("Progress ", completed , " / ", total , "users", end = "\r")
    
    for user in users:
        user_posts[user] = get_post_count(user)
        # print_ten_highest(user_posts)
        completed += 1
        print("Progress ", completed , " / ", total, "users",  end = "\r")

    print_sorted(user_posts)
    print("Samples : ", samples, "Time elapsed: ", time.time () - process_start , "s")


def print_ten_highest(user_posts):
    highest = sorted(user_posts, key = lambda x: user_posts[x], reverse = True)
    for rank, user in enumerate(highest[0:10]):
        print(rank + 1, " : ", user, " : ", user_posts[user])

def print_sorted(user_posts):
    highest = sorted(user_posts, key = lambda x: user_posts[x], reverse = True)
    for rank, user in enumerate(highest):
        print(rank + 1, " : " , user, " : ", user_posts[user])

def get_posts_from_page(soup):
    matches = soup.find_all("a", "thread-item-header-title")
    links = set()
    for match in matches:
        links.add(THREAD_ROOT + match.get("href"))
    
    return links



def get_user_names_from_link(link):
    users = set()
    #print("MAKING REQUEST FOR ", link)
    # print("Accessing ", link)
    soup = BeautifulSoup(requests.get(link).content, features = 'lxml')
    #print("GOT SOUP!")
    matches = soup.find_all("a", "post-header-author")
    
    for match in matches:
        users.add(match.text.strip())
    
    return users



def get_post_count(user):
    link = USER_ROOT + user
    # print("Accessing ", link)
    soup = BeautifulSoup(requests.get(link).content, features = 'lxml')
    matches = soup.find_all("tr")

    for match in matches:
        if "posts" in match.text.lower():
            posts = match.text.lower().strip()
            posts = int(posts.replace("Posts", "").replace("posts:", "").strip())
    return posts

get_user_posts(int(input("Enter sample size")))
#get_post_count("queueK")

