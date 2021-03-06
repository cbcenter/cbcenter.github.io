# encoding: utf-8
import os
import datetime
import json
import codecs
import markdown
import sys


def save_utf8(filename, text):
    with codecs.open(filename, 'w', encoding='utf-8')as f:
        f.write(text)


def load_utf8(filename):
    with codecs.open(filename, 'r', encoding='utf-8') as f:
        return f.read()


def savefinalhtml(filepath, finalhtml):
    output_file = codecs.open(filepath, "w", encoding="utf-8")
    output_file.write(finalhtml)
    output_file.close()
    print("success generate ", filepath)


# load templates
index = load_utf8("index_template.html")
banner = load_utf8("banner_template.html")
u8u4 = load_utf8("8u-4u.html")
personal = load_utf8("people/personal_template.html")

# siteMap = load_utf8("templates/sitemap.tm.xml")

# generate index
new_index = index.replace("{{TITLE}}", "CBMI Group")
index_body = ""
index_body = index_body + banner + u8u4

news = [
  ['images/GNMD.png', 'Blind Denoising of Fluorescence Microscopy Images Using GAN-Based Global Noise Modeling', 'We have developed a blind denoiser that uses one GAN to model image noise globally and another GAN to drastically reduce background noise.', 'https://biomedicalimaging.org/2021/'],
  ['images/wsbm.jpg', 'Dynamic Organization of Intracellular Organelle Networks', 'We have developed a method to assess quality of synthetic fluorescence microscopy images and to evaluate their training performance in image segmentation.', 'https://onlinelibrary.wiley.com/doi/10.1002/wsbm.1505'],
  ["https://ars.els-cdn.com/content/image/1-s2.0-S221112471830860X-mmc6.mp4", "Whole-Cell Scale Dynamic Organization of Lysosomes Revealed by Spatial Statistical Analysis", "Our findings reveal whole-cell scale spatial organization of lysosomes and provide insights into how organelle interactions are mediated and regulated across the entire intracellular space.", "https://www.sciencedirect.com/science/article/pii/S221112471830860X",
   "https://ars.els-cdn.com/content/image/1-s2.0-S221112471830860X-mmc6.jpg"],
  ["images/er-segmentation.png", "Deep Learning-Based Segmentation of Biological Networks in Fluorescence Microscopy", "We developed a deep learning-based pipeline to study the effects of image pre-processing, loss functions and model architectures for accurate segmentation of biological networks in FLMI.", "./projects/er-segmentation.html"],
  ["images/feng3-p5-feng-large.gif", "Quality Assessment of Synthetic Fluorescence Microscopy Images for Image Segmentation", "We have developed a method to assess quality of synthetic fluorescence microscopy images and to evaluate their training performance in image segmentation.", "https://ieeexplore.ieee.org/abstract/document/8802971"],
]

news_content = []
for a_new in news:
  if len(a_new) == 4: # news_template
    a_news_template = load_utf8("news_template.html")
    t_new = a_news_template.replace("{{IMG_URL}}", a_new[0])
    t_new = t_new.replace("{{RESEARCH_TITLE}}", a_new[1])
    t_new = t_new.replace("{{RESEARCH_BRIEF}}", a_new[2])
    t_new = t_new.replace("{{RESEARCH_LINK}}", a_new[3])
    news_content.append(t_new)
  elif len(a_new) == 5: # video_news
    t_video_template = load_utf8("video_news.html")
    t_new = t_video_template.replace("{{VIDEO_URL}}", a_new[0])
    t_new = t_new.replace("{{RESEARCH_TITLE}}", a_new[1])
    t_new = t_new.replace("{{RESEARCH_BRIEF}}", a_new[2])
    t_new = t_new.replace("{{RESEARCH_LINK}}", a_new[3])
    t_new = t_new.replace("{{VIDEO_IMG}}", a_new[4])
    news_content.append(t_new)
  else:
    pass


a_row = load_utf8("row_template.html")
more_research_row = load_utf8("more_research_row.html")

index_body = index_body + a_row.replace("{{INNER}}", news_content[0] + news_content[1]) + more_research_row
new_index = new_index.replace("{{BODY}}", index_body)
new_index = new_index.replace("{{COUNT}}", "")
savefinalhtml("index.html", new_index)


# generate research
pub = index.replace("{{TITLE}}", "Research")
pub_tem = load_utf8("style2_template.html")
publications = load_utf8("md/research.md")
publications = markdown.markdown(publications)
pub_content = pub_tem.replace("{{POST_TITLE}}", "Research Projects")
research_row = load_utf8("a_project_row.html")

research_content = ""
for a_content in news_content:
  research_content = research_content + a_content.replace('"4u"', '"6u"')

pub_content = pub_content.replace("{{POST_CONTENT}}", publications + research_row.replace("{{INNER}}", research_content))
pub = pub.replace("{{BODY}}", pub_content)
pub = pub.replace("{{COUNT}}", "research.html")
savefinalhtml("research.html", pub)

# generate people
pub = index.replace("{{TITLE}}", "Team")
my_people = load_utf8("md/people_template.html")
pub = pub.replace("{{BODY}}", my_people)
pub = pub.replace("{{COUNT}}", "people.html")
savefinalhtml("people.html", pub)

def generate_a_person(mdpath, pagetitle, htmlpath):
    pub = personal.replace("{{TITLE}}", pagetitle)
    pub_tem = load_utf8("style2_template.html")
    publications = load_utf8(mdpath)
    publications = markdown.markdown(publications)
    pub_content = pub_tem.replace("{{POST_TITLE}}", pagetitle)
    pub_content = pub_content.replace("{{POST_CONTENT}}", publications)
    pub = pub.replace("{{BODY}}", pub_content)
    count = htmlpath.replace("/", "%2F")
    pub = pub.replace("{{COUNT}}", count)
    savefinalhtml(htmlpath, pub)

person_infos = [
  # markdown_path, title, html_path
  ["md/yangge.md", "Ge Yang",       "people/geyang.html"],
  ["md/lwj.md",    "Wenjing",       "people/wenjingli.html"],
  ["md/gyh.md",    "Yuanhao Guo",   "people/yuanhaoguo.html"],
  ["md/yp.md",     "Ping Yang",     "people/pingyang.html"],
  ["md/lgl.md",    "Guole Liu",     "people/guoleliu.html"],
  ["md/lyr.md",    "Yaoru Luo",     "people/yaoruluo.html"],
  ["md/zlq.md",    "Liqun Zhong",   "people/liqunzhong.html"],
  ["md/xyp.md",    "Yunpeng Xiao",  "people/yunpengxiao.html"],
  ["md/wsy.md",    "Shiyu Wu",      "people/shiyuwu.html"],
  ["md/zyt.md",    "Yating Zhou",   "people/yatingzhou.html"],
  ["md/zyf.md",    "Yanfeng Zhou",  "people/yanfengzhou.html"],
  ["md/qmx.md",    "Mengxuan Qiu",  "people/mengxuanqiu.html"],
  ["md/zyd.md",    "Yudong Zhang",  "people/yudongzhang.html"],
  ["md/hj.md",     "Jia He",        "people/jiahe.html"],
]

# generate personal homepage.
for a_person in person_infos:
    generate_a_person(a_person[0], a_person[1], a_person[2])


# generate publications
pub = index.replace("{{TITLE}}", "Publications")
pub_tem = load_utf8("style2_template.html")
publications = load_utf8("md/publications_yangge.md")
publications = markdown.markdown(publications)
pub_content = pub_tem.replace("{{POST_TITLE}}", "Publications")
pub_content = pub_content.replace("{{POST_CONTENT}}", publications)
pub = pub.replace("{{BODY}}", pub_content)
pub = pub.replace("{{COUNT}}", "publications.html")
savefinalhtml("publications.html", pub)

# generate positions
pub = index.replace("{{TITLE}}", "Open Positions")
pub_tem = load_utf8("style2_template.html")
publications = load_utf8("md/positions.md")
publications = markdown.markdown(publications)
pub_content = pub_tem.replace("{{POST_TITLE}}", "Open Positions")
pub_content = pub_content.replace("{{POST_CONTENT}}", publications)
pub = pub.replace("{{BODY}}", pub_content)
pub = pub.replace("{{COUNT}}", "openpositions.html")
savefinalhtml("openpositions.html", pub)

# generate contacts
contacts = index.replace("{{TITLE}}", "Contact Us")
contact_tem = load_utf8("contact_template.html")
contact_html = contacts.replace("{{BODY}}", contact_tem)
contact_html = contact_html.replace("{{COUNT}}", "contact.html")
savefinalhtml("contact.html", contact_html)

project_tem = load_utf8("projects/project_template.html")
def generate_a_project(mdpath, pagetitle, htmlpath):
    pub = project_tem.replace("{{TITLE}}", pagetitle)
    article_tem = load_utf8("article_template.html")
    project_md = load_utf8(mdpath)
    project_content = markdown.markdown(project_md, extensions=['codehilite', 'fenced_code', 'extra'])
    article_content = article_tem.replace("{{POST_CONTENT}}", project_content)
    pub = pub.replace("{{BODY}}", article_content)
    count = htmlpath.replace("/", "%2F")
    pub = pub.replace("{{COUNT}}", count)
    savefinalhtml(htmlpath, pub)
# generate projects
projects_info = [
  # markdown_path, title, html_path
  ["md/er-segmentation.md", "ER Segmentation", "projects/er-segmentation.html"]
]

for a_project in projects_info:
    generate_a_project(a_project[0], a_project[1], a_project[2])
