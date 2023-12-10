# Hi 👋! My name is Alexander

I'm just here to learn and hopefully to become developer one day




---

<div align="center">
 <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/csharp/csharp-original.svg" height=50   width=62/>
  <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/rust/rust-plain.svg" height=50   width=62   alt="rust logo"     />
  <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/linux/linux-original.svg"         height="50" width="62" alt="linux logo"    />
  <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/git/git-original.svg"             height="50" width="62" alt="git logo"      />
  <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/arduino/arduino-original.svg"     height="50" width="62" alt="arduino logo"  />
</div>

```
trait PhraseOut {
    fn print_points(&self);
}

struct Phrase {
    phrase_text: String
}

impl PhraseOut for Phrase {
    fn print_points(&self) {
        println!("{}", self.phrase_text);
    }
}

fn main() {
    let _text = String::from("Hi 👋! My name is Alexander \n
   I'm just here to learn and hopefully to become developer one day ");

    let _phrase: Phrase = Phrase { phrase_text: _text};
    _phrase.print_points();
}

