import { useState } from "react";
import heroImg from "./assets/hero.png";
import reactLogo from "./assets/react.svg";
import GithubLogo from "./assets/github-142-svgrepo-com.svg";
import viteLogo from "./assets/vite.svg";
import TheThing from "./assets/TheThing.jpg";
import "./App.css";

function App() {
  const [count, setCount] = useState(0);

  return (
    <>
      <section id="center">
        <div className="hero">
          <img
            src={TheThing}
            className="base"
            width="170"
            height="179"
            alt=""
          />
        </div>
        <div>
          <h1>Первое взаимодействие с React</h1>
        </div>
        <button
          type="button"
          className="counter"
          onClick={() => setCount((count) => count + 2)}
        >
          Count is {count}
        </button>
      </section>

      <div className="ticks"></div>

      <section id="next-steps">
        <div id="docs">
          <svg className="icon" role="presentation" aria-hidden="true">
            <use href="/icons.svg#documentation-icon"></use>
          </svg>

          <p>Ссылка на гитхаб проекта и один видос</p>
          <ul>
            <li>
              <a
                href="https://github.com/Tankivan/InternetSafetySystemProject"
                target="_blank"
              >
                <img className="logo" src={GithubLogo} alt="" />
                Гитхаб
              </a>
            </li>
          </ul>
        </div>
        <div id="Youpoop">
          <h2> Ссылка на рандомный ютуб ролик</h2>
          <ul>
            <li>
              <a href="https://youtu.be/dQw4w9WgXcQ" target="_blank">
                Ссылка
              </a>
            </li>
          </ul>
        </div>
      </section>

      <div className="ticks"></div>
      <section id="spacer"></section>
    </>
  );
}

export default App;
