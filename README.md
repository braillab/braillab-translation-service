# Braille Translation Service

Convert text to braille cell dot positions in Grade 1 and 2.

## Supported (**v0.9**)

<div align=center>

|Languages|Grade 1|Grade 2|
|---------|-------|-------|
|Spanish| ✓ | |
|English| ✓ | ✓ |

</div>

**Grade 1** is uncontracted: letter by letter. **Grade 2** is contracted: with abbreviations.

<div align=center>

![Braulio (Braillab Icon and Honorary Team Member) Gif](images/braulio.gif)

</div>

## Language data format

The values ​​corresponding to the characters mapping the `template.json` are arrays representing the six dots of a Braille cell (for example, `a: [1]` or `l: [1,2,3]`).

<div align=center>

```bash
 1 ⬤ ⬤ 4 
2 ⬤ ⬤ 5
3 ⬤ ⬤ 6
```

</div>

There are also indicator characters, such as the capital sign (referred to here as `mayus`), which marks the beginning of a sentence or a capital letter, and the numeric indicator (`number`).

In addition, there are contractions, most notably in Unified English Braille where words like `"but"` are translated into the dots: `[1,2]`. When contractions exist, the `grade_supported` in the `language` should be set `2`.

```json
{
  "language": {
    "code": "es",
    "name": "Spanish",
    "native_name": "Español",
    "grade_supported": 1
  },
  "indicators": {
    "number": [3,4,5,6],
    "mayus": [4,6]
  },
  "letters": {
    "a": [1]
  },
  "numbers": {
    "0": [2,4,5]
  },
  "punctuation":{
    ".": [3]
  },
  "contractions": {}
}
```

For the `language` data, the expected code (the abbreviation and file name), such as `en` (English) or `es` (Spanish); the English name; and the native name (the name in the original language, such as "Español" for Spanish).

## Adding a new language

Fork the repository, then clone your fork and go to the project directory:

```bash
  git clone https://github.com/<your-username>/braillab-translation-service.git
  cd braillab-translation-service
```

Create and activate virtual environment (Python `3.13.5`).

```bash
  python -m venv venv
```

The activation command depends on your operating system.

- **macOS and Linux**: `source venv/bin/activate`
- **Windows (Command Prompt):** `venv\Scripts\activate.bat`
- **Windows (PowerShell):** `venv\Scripts\Activate.ps1`

Install the dependencies:

```bash
pip install -r requirements.txt
```

Copy the template (`_template.json`) and name the new file after the language code (see [language data format](#language-data-format)):

```bash
cp languages/_template.json languages/ex.json
```

Edit the file to match the braille code for that language.

Finally run the tests:

```bash
pytest --data_name="ex.json"
```

## Contributions

Feel free to push your changes to a new branch and open a **pull request**.  This automatically runs the existing tests, so there shouldn't be any issues. Should you grace this codebase with your labor, your legend will live on forever. Appreciate you 🫡.

![Braulio Idle Image](images/braulio_idle_sep.png)

## Team

Built by the Braillab team, Facultad de Ingeniería, Universidad Autónoma de Campeche:

- Christian Dominique Hernández Pacheco.
- María Fernanda Rincón Chan.
- Valeria de los Angeles Lee Almeyda. (Vibing)

Advisor: Joel Cristopher Flores Escalante.

![Braulio Happy Image](images/braulio_feliz_sep.png)

<p style="text-align: right;">... And let's not forget, Braulio!</p>