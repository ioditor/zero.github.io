# Zero Website — RU / EN

Статический сайт для https://github.com/ioditor/zero.github.io. Семь оригинальных примеров, раздел Шрифты/Fonts с Zero Flow, Still и Mono, Downloads, мобильное меню, SEO. Раздела документации нет. Сборка без npm и внешних зависимостей, Python 3.10+.

## Локальное превью

```sh
python build.py
python check.py
python preview.py
```

Откройте http://127.0.0.1:8000/zero.github.io/ru/#fonts или http://127.0.0.1:8000/zero.github.io/en/#fonts . Сервер слушает только этот компьютер; остановка Ctrl+C. На Windows можно использовать `py -3` вместо `python`. Если порт занят, измените 8000 в preview.py.

Готовые страницы также находятся в dist/ru/index.html и dist/en/index.html. Для проверки маршрутизации и сохранения языка используйте HTTP. Корень выбирает сохранённый язык, затем язык браузера. Переключение сохраняет позицию в видимом блоке, независимо от устаревшего якоря в адресе, и меняет все тексты и образцы.

## Исходники

- content.json — русский и английский тексты, включая образцы шрифтов.
- build.py — HTML, canonical/hreflang, Open Graph, sitemap и BASE.
- site/assets — CSS, JS, семь примеров на двух языках и локальные WOFF2.
- check.py — ссылки, пути CSS, шрифты, языки, контрольные суммы.
- material-manifest.json — контрольные суммы неизменённых исходных материалов.
- font-manifest.json, FONT-RIGHTS.md — состав шрифтов и основание использования.
- .github/workflows/pages.yml — CI и отдельно разрешаемая публикация.
- dist — результат сборки, включён для превью, исключён из Git.

TTF не включены; шрифты подключены только как ресурсы для отображения. Права подтверждены пользователем 18.10.2026; полная история проверки в FONT-RIGHTS.md. Открытая лицензия не заявляется.

Планируемый project URL: https://ioditor.github.io/zero.github.io/ . Репозиторий zero.github.io принадлежит ioditor, поэтому это project site с префиксом /zero.github.io/, а не корень домена. CNAME нет. Ассеты относительные. PDF и .zero сохранены как исходные материалы; галерея показывает семь локализованных PNG. Downloads ведёт на Releases. Сообщение об отсутствии релиза удалено по запросу владельца.

## Последующий push — только по решению владельца

Никаких commit, push, изменений настроек или запусков Actions в ходе этой работы не было.

1. Клонируйте репозиторий в отдельную папку и проверьте актуальное содержимое:

```sh
git clone https://github.com/ioditor/zero.github.io.git
cd zero.github.io
```

2. Перенесите содержимое zero-site, включая .github и .gitignore. Если репозиторий уже содержит файлы, объедините изменения после просмотра diff. Не копируйте чужую .git. Не используйте force push.
3. Запустите `python build.py` и `python check.py`, затем `git status` и `git diff`. Убедитесь, что ветка main и адрес origin верны.
4. После разрешения на push:

```sh
git add README.md FONT-RIGHTS.md font-manifest.json content.json build.py check.py preview.py material-manifest.json site .github .gitignore
git commit -m "Add bilingual Zero font specimens and Pages checks"
git push -u origin main
```

Push и pull request запускают build/check/upload artifact, но deploy пропускается. Это не публикация данного workflow; перед push проверьте, что в репозитории нет других автоматически публикующих workflows.

## Отдельная публикация — после явного разрешения

В Settings → Pages выберите Source: GitHub Actions. При необходимости задайте approvals для environment github-pages. В Actions → Build and manually deploy Zero Pages → Run workflow выберите main и включите publish. Без этого флага deploy не запускается. После реального запуска проверьте логи и обе языковые страницы по адресу deployment.

Workflow содержит checkout, Python build/check, upload-pages-artifact; deploy зависит от build и получает pages:write/id-token:write. Использует configure-pages и deploy-pages, environment github-pages и page_url.

Справочник: https://docs.github.com/en/pages/getting-started-with-github-pages/using-custom-workflows-with-github-pages . Локальная проверка не доказывает успешный запуск GitHub Actions, доступность Pages или правильность настроек удалённого репозитория.

## Бумажный Zero / Zero on Paper

Раздел #paper: заголовок и ссылка на локализованный PDF с метками сгиба. Шаблон — paper_section.py, материалы — site/assets/paper/. Дополнительные PDF, PNG и .zero из архива сохранены как материалы, но не выведены в интерфейсе.
