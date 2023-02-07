const url = "./data.json";
document.addEventListener("DOMContentLoaded", () => {
  getHeader();
  renderingHeader();
});

async function renderingHeader() {
 const header = await getHeader();
 console.log(header);
  const encabezado = document.querySelector("#bar");

  let html = "";
  html = `
        <nav>
        <ul class="topnav">
          <li><a class="active" href="#">${header.header[0].title}</a></li>
          <li class="right"><a href="#">${header.header[4].nav4}</a></li>
          <li class="right"><a href="#">${header.header[3].nav3}</a></li>
          <li class="right"><a href="#">${header.header[2].nav2}</a></li>
          <li class="right"><a href="#">${header.header[1].nav1}</a></li>
        </ul>
      </nav>
        `;
  encabezado.innerHTML = html;
}

async function getHeader() {
    try {
        const resultado = await fetch(url);
        const navs = await resultado.json();
        return navs;
    } catch (error) {
        console.log(error);
        
    }
}
