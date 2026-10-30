#!/usr/bin/env python3
"""Generate the public CV without confidential project details or private phone numbers."""
from pathlib import Path
import json
from xml.sax.saxutils import escape
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, PageBreak, KeepTogether
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.colors import HexColor
from reportlab.lib.enums import TA_LEFT
R=Path(__file__).resolve().parents[1]
d=json.loads((R/'content/site.json').read_text())
styles=getSampleStyleSheet()
styles.add(ParagraphStyle(name='Name',fontName='Times-Roman',fontSize=31,leading=34,textColor=HexColor('#223c33'),spaceAfter=10))
styles.add(ParagraphStyle(name='Label',fontName='Helvetica-Bold',fontSize=10,leading=14,textColor=HexColor('#256f60'),spaceBefore=16,spaceAfter=9))
styles.add(ParagraphStyle(name='BodyCV',fontName='Helvetica',fontSize=9.3,leading=13.3,textColor=HexColor('#34433c'),spaceAfter=8))
styles.add(ParagraphStyle(name='Entry',fontName='Helvetica-Bold',fontSize=10.5,leading=14,spaceBefore=9,spaceAfter=4))
styles.add(ParagraphStyle(name='Meta',fontName='Helvetica',fontSize=8.5,leading=12,textColor=HexColor('#657269'),spaceAfter=6))
flow=[]
def p(s,style='BodyCV'):flow.append(Paragraph(s,styles[style]))
def sec(s):p(s.upper(),'Label')
def entry(name,meta,text):
 flow.append(KeepTogether([Paragraph(name,styles['Entry']),Paragraph(meta,styles['Meta']),Paragraph(text,styles['BodyCV'])]))
p('Shaoyang Zhang','Name')
p('Computer Science · University of Michigan, Ann Arbor','Meta')
p('<link href="mailto:onionzsy@umich.edu">onionzsy@umich.edu</link>  |  <link href="https://oniongreen123.github.io">oniongreen123.github.io</link>  |  <link href="https://github.com/OnionGreen123">GitHub</link>  |  <link href="https://www.linkedin.com/in/shaoyang-zhang-82861a33b">LinkedIn</link>','Meta')
sec('Research interests')
p('Mechanistic interpretability, world-model safety, adversarial robustness, cognition-aware AI, and human–AI interaction.')
sec('Education')
entry('University of Michigan, Ann Arbor','B.S.E. in Computer Science | Aug 2025 – May 2027 (expected)','Cheng Family Scholarship (2025); Dean’s List.')
entry('Shanghai Jiao Tong University','B.E. in Mechanical Engineering | Aug 2023 – Aug 2027 (expected)','Academic Excellence Scholarship (2024). President, ASME UMJI Student Chapter; Vice President, Students Science &amp; Technology Innovation Association.')
sec('Research experience')
entry('Northwestern University','Undergraduate Research Assistant · Remote | Mar 2026 – Present','Lead ongoing research on world-model hijacking and targeted adversarial attacks that aim to steer model behavior toward an attacker-chosen objective. Contributed controlled interventions and layer-wise representation analysis to research on attention sinks and activation outliers.')
entry('Michigan Institute for Data and AI in Society (MIDAS)','Undergraduate Research Assistant · Ann Arbor | Oct 2025 – Sep 2026','Mentors: Prof. Q. Vera Liao and Dr. Yoonjoo Lee. Built conversation-analysis pipelines and experimental infrastructure for knowledge-state-aware user simulation, including information-unit extraction, state updates, user-query generation, and evaluation. Implemented the initial end-to-end human validation-study system, including the chat interface, response collection, participant progress tracking, and data logging. Iterated through pilot feedback and failure analysis.')
entry('Data-informed Design and Intelligent Systems Laboratory','Undergraduate Research Assistant · Shanghai | Oct 2024 – Oct 2025','Mentors: Prof. Youyi Bi and Dr. Chang Liu. Studied imitation learning for robotic manipulation; reproduced and evaluated MimicPlay. Independently developed keyboard-based robotic-arm teleoperation to collect human demonstration trajectories.')
flow.append(PageBreak())
p('Shaoyang Zhang','Name');p('Publications & selected projects','Meta')
sec('Publications')
for pub in d['publications']:
 title=escape(pub['title']);author=escape(pub['authors']).replace('Shaoyang Zhang','<b>Shaoyang Zhang</b>')
 link=next(iter(pub['links'].values()))
 flow.append(KeepTogether([Paragraph(title,styles['Entry']),Paragraph(author,styles['BodyCV']),Paragraph(escape(pub['venue']+' · '+pub['extra']),styles['Meta']),Paragraph(f'<link href="{link}" color="#256f60">{link}</link>',styles['Meta']),Spacer(1,5)]))
p('* Equal contribution. OASIS author ordering follows the current public paper.','Meta')
sec('Selected engineering projects')
entry('Robotic-arm teleoperation','DIDIS Laboratory','Developed keyboard-based teleoperation and collected demonstration trajectories for imitation learning experiments.')
entry('DATA TAMER','EECS 448 team project · In development, Fall 2026','Exploring StarCraft II win-probability prediction and attribution using spatial sequences and structured game-state features.')
def footer(c,doc):
 c.setStrokeColor(HexColor('#dcded6'));c.line(47,42,565,42);c.setFont('Helvetica',8);c.setFillColor(HexColor('#657269'));c.drawString(47,29,'Public CV · Updated 29 October 2026');c.drawRightString(565,29,str(doc.page))
doc=SimpleDocTemplate(str(R/'assets/Shaoyang_Zhang_CV.pdf'),pagesize=(612,792),leftMargin=47,rightMargin=47,topMargin=42,bottomMargin=57,title='Shaoyang Zhang — Curriculum Vitae',author='Shaoyang Zhang')
doc.build(flow,onFirstPage=footer,onLaterPages=footer)
print('Created public CV')
