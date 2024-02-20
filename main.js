const { exec } = require("child_process");

// Comando para chamar o script Python
const command = "excel_to_json.py";

// Executando o script Python
exec(command, (error, stdout, stderr) => {
  if (error) {
    console.error(`Erro ao executar o script: ${error}`);
    return;
  }
  console.log(`Saída do script Python: ${stdout}`);
});
