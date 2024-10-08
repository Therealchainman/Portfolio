# utils.py

def html_anchor_generator(prefix, domain, icon_link, username = None, repo = None):
    link = f"{prefix}{domain}"
    if username:
        link += f"/{username}"
    if repo:
        link += f"/{repo}"
    hyperlink = f"href = {link}>"
    image = f"<img src = {icon_link} width = 30>"
    html_anchor_element = f"<a {hyperlink}{image}</a>"
    print(html_anchor_element)
    return html_anchor_element