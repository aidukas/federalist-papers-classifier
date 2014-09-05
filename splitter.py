import io, json

text = open('The Federalist Papers.txt').readlines()
text = ''.join(text)

split_text = text.split('FEDERALIST No. ')[1:]

split_text[84] = split_text[84].split("End of the Project Gutenberg EBook of The Federalist Papers, by")[0]

Hamilton = []
Jay = []
Madison = []
Disputed = []

i = 0
while i < 85:
  tex = split_text[i]
  
  number = int(tex.split('\r\n\r\n')[0])
  
  if number >=62 and number <= 63:
    Disputed.append(tex)
  elif number >= 49 and number <=58:
    Disputed.append(tex)
  elif number >=18 and number <=20:
    Madison.append(tex)
  else:
    if 'HAMILTON' in tex:
      Hamilton.append(tex)
    elif 'JAY' in tex:
      Jay.append(tex)
    elif 'MADISON' in tex:
      Madison.append(tex)
  i+=1

papers = {'Hamilton':Hamilton, 'Jay':Jay, 'Madison':Madison, 'Disputed':Disputed}


for k in papers.keys():
  print k
  print len(papers[k])



with open('papers.txt', 'w') as outfile:
  json.dump(papers, outfile)
