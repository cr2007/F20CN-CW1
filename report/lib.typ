#let template(doc) = [
  #set page(
    header: [
      Computer Network Security
      #h(1fr)
      cr2007
    ],
    footer: [
      F20CN
      #h(1fr)
      #context counter(page).display("1")
      #h(1fr)
      Coursework 1
    ],
  )

  #set text(font: "Segoe UI")

  #set align(center)

  #show link: underline

  #show outline.entry.where(level: 1): it => {
    v(12pt, weak: true)
    text(it)
  }

  #doc
]
