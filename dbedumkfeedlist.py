#!/usr/bin/env python
# -*- coding: UTF-8 -*-
#

def mkopmlfeedlist():
	import dbeduwdpfeed
	blog_list = dbeduwdpfeed.blog_list
	folders = concatenate_feed_folder(blog_list)
	feedlist_opml='''<?xml version="1.0"?>
	<opml version="1.0">
	  <head>
		<title>%s</title>
	  </head>
	  <body>
		%s
	  </body>
	</opml>
	''' % ('Blogs CED01 - Planaltina', folders)
	return feedlist_opml
	
def concatenate_feed_folder(blog_stored_list):
	folder=''
	for i in blog_stored_list:
		feedlist = concatenate_feed(blog_stored_list,i,serverIP='localhost')
		folder = folder + '''    <outline title="%s" text="%s" description="%s" type="folder">
      %s
    </outline>
	''' % (i,i,i,feedlist)
	return folder

def concatenate_feed(blog_stored_list,turma,serverIP):
	feed=''
	for i in blog_stored_list[turma]:
		feed = feed + '''      <outline title="%s" text="%s" description="%s" type="rss" xmlUrl="http://%s/wdp/%s/?feed=rss2" htmlUrl="http://%s/wdp/%s"/>
		''' % (i[0],i[0],i[0],serverIP,i[1],serverIP,i[1])
	#print feed + '\n\n'
	return feed

duca = mkopmlfeedlist()

f = open('daniel.opml','w')
f.write(duca)
f.close()
