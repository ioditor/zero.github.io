def paper_section(lang):
 ru=lang=='ru'
 title='Бумажный Zero' if ru else 'Zero on Paper'
 label='PDF с метками сгиба' if ru else 'PDF with fold marks'
 return f'<section class="section" id="paper"><div class="heading"><div><p class="eyebrow">ZERO PAPER GUIDE / 0.1</p><h2>{title}</h2></div></div><a class="button" href="../assets/paper/Zero-Brochure-{lang.upper()}-folds.pdf" download>{label}</a></section>'
