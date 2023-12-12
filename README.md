---

<div align="center">
 <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/csharp/csharp-original.svg" height=50   width=62/>
  <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/rust/rust-plain.svg" height=50   width=62   alt="rust logo"     />
  <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/linux/linux-original.svg"         height="50" width="62" alt="linux logo"    />
  <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/git/git-original.svg"             height="50" width="62" alt="git logo"      />
  <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/cplusplus/cplusplus-original.svg" />
  <=        
 <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/arduino/arduino-original.svg"     height="50" width="62" alt="arduino logo"  />
</div>

```
trait PhraseOut {
    fn print_phrase(&self);
}

struct Phrase {
    phrase_text: String
}

impl PhraseOut for Phrase {
    fn print_phrase(&self) {
        println!("{}", self.phrase_text);
    }
}

fn main() {
    let _text = String::from("Hi 👋! My name is Alexander \n \
    I'm just here to learn and hopefully to become developer one day ");
    let _phrase: Phrase = Phrase { phrase_text: _text};
    _phrase.print_phrase();
}

```

<div align="center">
  <img src="https://streak-stats.demolab.com?user=whuzurbuddha&locale=en&mode=daily&theme=radical&=true&border_radius=5" height="150" alt="streak graph" /> <br>
  <img src="https://github-readme-stats.vercel.app/api?username=whuzurbuddha&repo=whuzurbuddha&hide_title=false&hide_rank=false&show_icons=true&include_all_commits=true&count_private=true&disable_animations=false&theme=radical&locale=en&hide_border=false" height="150" alt="stats graph" /> <br> 
  <img src="https://github-readme-stats.vercel.app/api/top-langs?username=whuzurbuddha&repo=whuzurbuddha&locale=en&hide_title=false&layout=compact&card_width=320&langs_count=5&theme=radical&hide_border=false" height="150" alt="languages graph"  />
</div>

