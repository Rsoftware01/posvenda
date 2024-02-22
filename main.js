// Função para fazer a chamada à API e preencher os resultados na página HTML
async function fetchData() {
  // Realiza a requisição GET para o arquivo data.json
  const response = await fetch("./data.json");
  const data = await response.json();

  // Log dos dados obtidos para verificar a estrutura
  console.log("Dados obtidos do arquivo data.json:", data);

  // Mapeia os dados para extrair apenas os valores da coluna "Fixing"
  const fixingDates = data.map((item) => item["Data hoje"]);

  // Log dos dados da coluna "Fixing" antes da remoção de duplicatas
  console.log(
    "Datas da coluna 'Fixing' antes da remoção de duplicatas:",
    fixingDates
  );

  // Remove duplicatas das datas mantendo apenas uma ocorrência de cada valor único
  const uniqueFixingDates = Array.from(new Set(fixingDates));

  // Log dos dados da coluna "Fixing" após a remoção de duplicatas
  console.log(
    "Datas da coluna 'Fixing' após a remoção de duplicatas:",
    uniqueFixingDates
  );

  // Converter as datas para o formato Date e obter o dia da semana correspondente
  uniqueFixingDates.forEach((dateString) => {
    // Separar a string da data em partes (dia, mês e ano)
    const parts = dateString.split("/");
    // Construir um objeto Date (ano, mês, dia)
    const date = new Date(parts[2], parts[1] - 1, parts[0]);
    // Obter o nome do dia da semana
    const dayOfWeek = date.toLocaleDateString("pt-BR", { weekday: "long" });
    console.log(`Data: ${dateString}, Dia da semana: ${dayOfWeek}`);
  });

  // Retorna os dados obtidos
  return data;
}

// Função para filtrar e exibir os resultados da tabela
async function showResults() {
  // Obtém o valor selecionado no select
  const selectedName = document.getElementById("assessor").value;

  // Obtém os dados da tabela
  const data = await fetchData();

  // Filtra os dados da tabela com base no nome selecionado
  const filteredData = data.filter(
    (item) => item["Operador(a)"] === selectedName
  );

  // Obtém a referência do elemento onde os resultados serão exibidos
  const resultadoDiv = document.getElementById("resultado");

  // Limpa o conteúdo atual da div de resultados
  resultadoDiv.innerHTML = "";

  // Se houver resultados filtrados, cria uma tabela e preenche com os dados
  if (filteredData.length > 0) {
    const table = document.createElement("table");
    table.classList.add("w-full", "my-4", "text-white");

    // Cria o cabeçalho da tabela
    const headerRow = table.insertRow();
    Object.keys(filteredData[0]).forEach((key) => {
      const headerCell = document.createElement("th");
      headerCell.textContent = key;
      headerRow.appendChild(headerCell);
    });

    // Preenche a tabela com os dados filtrados
    filteredData.forEach((item) => {
      const row = table.insertRow();
      Object.values(item).forEach((value) => {
        const cell = row.insertCell();
        cell.textContent = value;
      });
    });

    // Adiciona a tabela à div de resultados
    resultadoDiv.appendChild(table);
  } else {
    // Se não houver resultados, exibe uma mensagem de "Nenhum resultado encontrado"
    resultadoDiv.textContent = "Nenhum resultado encontrado.";
  }
}

// Função principal que será chamada quando a página for carregada
window.onload = function () {
  // Adiciona um evento de clique ao botão "Mostrar" para mostrar os campos adicionais
  const mostrarCamposBtn = document.getElementById("mostrar-campos-adicionais");
  mostrarCamposBtn.addEventListener("click", async (event) => {
    // Evita o comportamento padrão do botão (enviar formulário)
    event.preventDefault();

    // Chama a função para mostrar os resultados e campos adicionais
    await showResults();
  });
};
