---
permalink: /
title: Complex Data Lab
layout: splash
header:
    overlay_image: /assets/images/trottier.webp
    actions:
        - label: "GitHub"
          url: "https://github.com/ComplexData-MILA"
        - label: "Twitter"
          url: "https://x.com/complexDataLab"
        - label: "LinkedIn"
          url: "https://www.linkedin.com/company/complex-data-lab-mcgill-mila"

excerpt: "A research group focusing on developing techniques for analyzing complex data from online societies, with applications to enhance the health and safety of online spaces."

row_research:
  - image_path: /assets/images/home/group-photo-2.webp
    url: /publications
    alt: "Poster Presentation"
    title: "Research"
    btn_label: "Publications"
    btn_class: "btn--primary"
    excerpt: "We work on various topics and present our works in ML and NLP conferences and journals."

---

{% include research-directions.html category="research-directions"%}

{% include feature_row id="row_research" type="left" %}
