"""Jan Hus, De ecclesia (1413), in the English translation of David S. Schaff:
John Huss, De Ecclesia. The Church (New York: Charles Scribner's Sons, 1915).
Public domain.

Internet Archive deecclesiachurch00husjuoft (University of Toronto; printed
page n = leaf n+51). Read against the page images. Schaff's English is kept
as printed, with his bracketed references to Friedberg's Corpus iuris
canonici; his footnotes are not carried. The Latin is not given: the only
critical edition, S. Harrison Thomson's (Boulder 1956), is in copyright, and
the sixteenth-century printings are not available in usable scans. Where the
council condemned a sentence from the book, the Latin article is in the
module 'The council's decrees' (Decr. Articles). Cuts are marked [...].

Each unit: pg (Schaff page), titel, en, note."""

CHURCH = [
 {"pg": "3",
  "titel": "The Church of the predestinate",
  "en": "But the holy catholic—that is, universal—church is the totality of the predestinate—omnium predestinatorum universitas—or all the predestinate, present, past, and future. This definition follows St. Augustine on John, C. Recur. 32 : 4 [Friedberg, 1 : 1126], who shows how it is that one and the same church of the predestinate, starting at the beginning of the world, runs on to the apostles, and thence to the day of judgment. For Augustine says: \"The church which brought forth Abel, Enoch, Noah and Abraham, also brought forth Moses, and at a later time the prophets before the Lord's advent and she, which brought forth these, also brought forth the apostles and our martyrs and all good Christians. For she has brought forth all who have been born and lived at different periods, but they have all been comprised in a company of one people. And the citizens of this city have experienced the toils of this pilgrimage. Some are experiencing them now, and some will be experiencing them, even to the end of the world.\"",
  "note": "Chapter 1, the definition on which the whole book rests, and the first article condemned at Constance (Decr. Articles [1]). If the Church is the number of the predestined, known only to God, then no visible office, not even the papacy, makes anyone a member of it. Hus follows Wyclif here, and claims Augustine for both."},
 {"pg": "135–136",
  "titel": "Christ, the head, nearer than the pope",
  "en": "For it remains for them to prove that the pope is the head of holy church, a thing they have not proved. And, before that, it remains for them to prove that Christ is not the bodily head of the church militant, inasmuch as Christ is a bodily person, because the man who is the head of the church militant, who is Christ, is present through all time with his church unto the consummation of the age, in virtue of his divine personality. Similarly, he is present by grace, giving his body to the church to be eaten in a sacramental and spiritual way. Wherefore, is not that bridegroom, who is the head of the church, much more present with us than the pope, who is removed from us two thousand miles and incapable of influencing of himself our feeling or movements? Let it suffice, therefore, to say, that the pope may be the vicar of Christ and may be so to his profit, if he is a faithful minister predestinated unto the glory of the head, Jesus Christ.",
  "note": "Written in exile in southern Bohemia, against the eight Prague doctors (among them Páleč and Stanislav of Znojmo) who had declared the pope the head of the Church and the cardinals its body. 'Two thousand miles': the pope, John XXIII, sat in Rome. Hus does not deny that a pope may be Christ's vicar; he makes it conditional on his life."},
 {"pg": "143",
  "titel": "'The vicar of Judas'",
  "en": "From these and other sayings it is evident that no pope is the manifest and true successor of Peter, the prince of the apostles, if in morals he lives at variance with the principles of Peter; and, if he is avaricious, then is he the vicar of Judas, who loved the reward of iniquity and sold Jesus Christ. And by the same kind of proof the cardinals are not the manifest and true successors of the college of Christ's other apostles unless the cardinals live after the manner of the apostles and keep the commands and counsels of our Lord Jesus Christ. For, if they climb up by another way than by the door of our Lord Jesus Christ, then are they thieves and robbers, just as the Saviour himself declared when of all such he said: \"All that came before me are thieves and robbers,\" John 10 : 8. Whosoever, therefore, say that they are Christ's true and manifest vicars, knowing that they are living in sin, lie.",
  "note": "Chapter 13. The council condemned the substance of this as article 13 ('the pope is not the manifest and true successor of Peter if he lives contrary to Peter'). A month before the sentence the same council had deposed John XXIII for simony and worse: it judged the man as Hus would have, and condemned the principle."},
 {"pg": "211",
  "titel": "'To rebel against an erring pope is to obey Christ'",
  "en": "In view of these things it is to be held that to rebel against an erring pope is to obey Christ the Lord, because in making his provisions he chiefly makes those which savor of personal affection. Therefore, I call the world to witness that the papal distribution of benefices sows in the church hirelings all too widely. On the part of the popes, it gives them occasion to exalt their vicarial power, to put an excessive value on the world's dignity and to make an extravagant show of a fantastic sanctity. But these doctors, who are looking for temporal remuneration from the pope or servilely fear his power, and also are saying that he has mysterious power and is impeccable and inerrant and that he may do lawfully whatsoever pleases him—these doctors are pseudo-prophets and pseudo-apostles of antichrist.",
  "note": "Chapter 18, on the apostolic see. The sentence on rebellion was the one his accusers quoted most; in context it concerns the papal provision of benefices, the system by which the pope appointed to church offices across Christendom and took their revenues."},
 {"pg": "221–222",
  "titel": "'We must obey God rather than men'",
  "en": "Therefore, no one should obey man in anything, even the least thing, that opposes itself to the divine commands, which St. Bernard calls divine counsels. For Peter says: \"We must obey God rather than men,\" Acts 5 : 29. Hence, as we are commanded to obey our superiors in things lawful and honorable, with the circumstances taken into consideration, so we are commanded to resist them to the face when they walk contrary to the divine counsels or commandments. For Paul, teaching that we should be his imitators, I Cor. 4 : 16, withstood Peter to the face for a light offence, Gal. 2 : 11. [...] Therefore, the wise inferior ought to examine into the commands of a superior when he seems to deviate from Christ's law, or his rule. For no superior is above correction.",
  "note": "Chapter 19, on obedience. The principle Hus applied to himself at Constance: he would submit to the council if shown his error from scripture, but would not abjure against his conscience (Letters [4]). It is also the principle the Bohemian lords and the Prague towns took up after his death."},
]

SECTIONS = [
    {"id": "church", "zk": "De eccl.", "titel": "De ecclesia: the Church, the pope, obedience",
     "blurb": "Five passages from the treatise Hus wrote in exile in 1413, the book from which the council drew most of the articles it condemned: the Church as the number of the predestined, Christ its only head, the avaricious pope as the vicar of Judas, rebellion against an erring pope as obedience to Christ, and obedience to God before men.",
     "units": CHURCH},
]
