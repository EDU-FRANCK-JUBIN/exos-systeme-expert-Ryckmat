from pyDatalog import pyDatalog
pyDatalog.clear()

# pyDatalog.create_terms('grenouille','manges_des_mouches','croasse','X',
# 'gazouiller','chanter','canarie','vert','jaune')
#
# +croasse("fritz")
# +manges_des_mouches("fritz")
#
# grenouille(X) <= manges_des_mouches(X) & croasse(X)
#
# print(grenouille(X))
#
# +gazouiller("julien")
# +chanter("julien")
# canarie(X) <= gazouiller(X) & chanter(X)
# print(canarie(X))
# vert(X) <= grenouille(X)
# jaune(X) <= canarie(X)
# print(pyDatalog.ask('green(X)'))
#
#

# pyDatalogload("""
# trois_cote(X,Y,Z,A,B,C)
# sum_angle(A,B,C) <= (A + B) + C == 180
# deux_cote_egaux(X,Y,Z,A,B,C) <= X==Y || Y==Z || X==Z
# trois_cote_egaux(X,Y,Z,A,B,C) <= X==Y==Z
# angle_droit(X,Y,Z,A,B,C) <= A == 90 || B = 90 || C = 90
# triangle(X,Y,Z,A,B,C) <= trois_cote(X,Y,Z) & sum_angle(A,B,C)
# isocele(X,Y,Z,A,B,C) <= triangle(X,Y,Z,A,B,C) & deux_cote_egaux(X,Y,Z,A,B,C)
# equilateral(X,Y,Z,A,B,C) <= triangle(X,Y,Z,A,B,C) & trois_cote_egaux(X,Y,Z,A,B,C)
# rectange(X,Y,Z,A,B,C) <= triangle(X,Y,Z,A,B,C) & angle_droit(X,Y,Z,A,B,C)
# """)



# pyDatalog.create_terms('homme'
# 'femme',
# 'father',
# 'mother',
# 'Parent',
# 'Child',
# 'son_of',
# 'daughter_of', 'grandparent_of',
# 'GrandChild',
# 'GrandParent',
# 'GrandChild',
# 'Someone',
# 'ancestor_of',
# 'Descendant',
# 'Ancestor',
# 'X',
# 'ancestor_of2')
#
# homme("terah")
# homme("abraham")
# homme("nahor")
# homme("haran")
# homme("isaac")
# homme("ismael")
# homme("javob")
# femme("sarah")
# femme("hagar")
# father("terah","sarah")
# father("terah","abraham")
# father("abraham","isaac")
# father("isaac","jacob")
# father("abraham","ismael")
# mother("sarah","isaac")
# mother("hagar","ismael")
# parent(Parent,Child) <= father(Parent,Child)
# parent(Parent,Child) <= mother(Parent,Child)
# son_of(Child,Parent) <= homme(Child) & parent(Parent,Child)
# daughter_of(Child,Parent) <= femme(Child) & parent(Parent,Child)
# grandparent_of(GrandChild,GrandParent) <= distinct((GrandParent,GrandChild),(parent(GrandParent,Someone)),parent(Someone,GrandChild))
# ancestor_of(Descendant,Ancestor) <= parent(Ancestor,Descendant)
# ancestor_of(Descendant,Ancestor) <= parent(Ancestor,X),ancestor_of(Descendant,X)
# ancestor_of2(Descendant,Ancestor) <= distinct((Ancestor,Descendant), parent(Ancestor,Descendant))
# ancestor_of2(Descendant,Ancestor) <= distinct((Ancestor,Descendant), (parent(Ancestor,X),ancestor_of2(Descendant,X))
