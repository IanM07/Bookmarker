#Opens both files for use
bookmarks = open('bookmarks.html', 'w')
links = open('links.txt', 'r').readlines()

#Asks the user for bookmark folder title
folder_title = input('Please enter the bookmark folder title: ')

#Sets up the template for the bookmarks.html file
html_template = """<!DOCTYPE NETSCAPE-Bookmark-file-1>
    <META HTTP-EQUIV="Content-Type" CONTENT="text/html; charset=UTF-8">
    <TITLE>Bookmarks</TITLE>
    <H1>Bookmarks</H1>
    <DL><p>
        <DT><H3>{}</H3>
        <DL><p>
    """.format(folder_title)

#Begin looping through the list of links
for line in links:
    #Print link and ask for bookmark title
    print(line)
    title = input('Please enter a title for this bookmark: ')
    
    #Properly formats the link and title before adding to the HTML template
    new_link = """<DT><A HREF="{}">{}</A>""".format(line.strip('\n'), title)
    html_template = html_template + new_link + '\n'

#Finish the HTML template by adding the final HTML tags
html_template = html_template + "</DL><p>"
html_template = html_template + "</DL><p>"

#Write the gathered information to the bookmarks.html file before closing both files and exiting
bookmarks.write(html_template)
bookmarks.close()
links.close()
exit()
