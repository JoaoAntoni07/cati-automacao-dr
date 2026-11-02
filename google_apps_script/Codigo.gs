function processarNovoDocumento(textoDoArquivo, nomeDoArquivo) {
  // 1. URL atual do túnel + rota
  var urlDaSuaAPI = "";
  
  // 2. COLE AQUI O ID DA PASTA 'RESPOSTAS'
  var idPastaSaidas = ""; 
  
  var payload = {
    "texto": textoDoArquivo
  };
  
  var opcoes = {
    "method": "post",
    "contentType": "application/json",
    "headers": {
      "Bypass-Tunnel-Reminder": "true" // Evita a tela de bloqueio intermediária do localtunnel
    },
    "payload": JSON.stringify(payload),
    "muteHttpExceptions": true
  };
  
  try {
    Logger.log("Enviando " + nomeDoArquivo + " para a API Python...");
    var resposta = UrlFetchApp.fetch(urlDaSuaAPI, opcoes);
    var json = JSON.parse(resposta.getContentText());
    
    if (json.status === "sucesso") {
      Logger.log("Requisitos gerados com sucesso! Salvando no Drive...");
      
      var pastaDestino = DriveApp.getFolderById(idPastaSaidas);
      var nomeBase = nomeDoArquivo.replace(".txt", "").replace(".pdf", "");
      var nomeFinal = nomeBase + "_requisitos.md";
      
      // Cria o arquivo Markdown na pasta Respostas
      pastaDestino.createFile(nomeFinal, json.documento_gerado, MimeType.PLAIN_TEXT);
      Logger.log("Arquivo criado com sucesso: " + nomeFinal);
      
      return json.documento_gerado;
    } else {
      Logger.log("Erro retornado pela API: " + resposta.getContentText());
    }
  } catch (erro) {
    Logger.log("Falha na comunicação com o túnel: " + erro);
  }
}

function verificarPastaEntradas() {
    // preencher com os ids
  var idPastaEntradas = "";
  var idPastaProcessados = "";
  
  var pastaEntradas = DriveApp.getFolderById(idPastaEntradas);
  var pastaProcessados = DriveApp.getFolderById(idPastaProcessados);
  var arquivos = pastaEntradas.getFiles();
  
  while (arquivos.hasNext()) {
    var arquivo = arquivos.next();
    var nomeDoArquivo = arquivo.getName();
    
    Logger.log("Lendo arquivo novo: " + nomeDoArquivo);
    var textoDoArquivo = arquivo.getBlob().getDataAsString();
    
    // Processa na API Python e salva na pasta Respostas
    processarNovoDocumento(textoDoArquivo, nomeDoArquivo);
    
    // Move o arquivo bruto original para a pasta Processados
    arquivo.moveTo(pastaProcessados);
    Logger.log("Arquivo movido para Processados.");
  }
}