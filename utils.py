# utils.py

def html_anchor_generator(domain, icon_link, username = None, repo = None):
    link = f"https://{domain}"
    if username:
        link += f"/{username}"
    if repo:
        link += f"/{repo}"
    hyperlink = f"href = {link}>"
    image = f"<img src = {icon_link} width = 30>"
    html_anchor_element = f"<a {hyperlink}{image}</a>"
    return html_anchor_element