Segue um breve relatório de desenvolvimento do código.


Dei início ao projeto pesquisando sobre os novos termos hash e md5. Logo após comecei a pesquisa de como implementar uma função para verificar o md5 de arquivos. Encontrei um código simples que funcionava, porem era necessário o arquivo baixado para fazer a verificação. Mesmo assim ele ainda foi útil para entender como funciona o hash no python.

Depois de pesquisar encontrei um código no stackoverflow de uma pessoa que comparava um md5 de um arquivo local com o de um arquivo local na máquina dele. Então decidir usar a parte do código que me era interessante e adequei ao meu código.

Comecei então a analisar o código fonte do site do stf para tentar implementar o request, juntamente da biblioteca beautifulsoup.

Tive problemas de acesso ao site através do request que foi resolvido com a implementação de headers na função “montar_link”

A função gerar_md5 funcionava com outros links porem não com o do stf, logo percebi que se tratava do mesmo problema anterior então implementei os headers nessa função também.

Consegui fazer o código funcionar porem somente para datas que continha apenas um diário, esse problema foi resolvido através de try/except no qual ao identificar somente 1 diario na busca a função retornava as variáveis referentes aos outros diários como NONE.

Até então só havia feito testes com diários recentes, no caso esses com número de identificação com 3 caracteres (204	13/10/2021), os diários com menos que isso geravam erro, para resolver isso implementei if/elif que identificavam essa situação e adicionavam os “zeros” necessários.

A partir daqui todos os testes feitos funcionaram e dei como finalizado o código.

OBS: Em pesquisa ao site STF, percebi que o número máximo de diários em um dia tinha sido 2, então implementei o código de forma que retorne no máximo 3 hashs md5.
Os testes foram feitos de forma manual e com ajuda do site OnlineMD5 (http://onlinemd5.com/)
As fontes utilizadas se baseiam em vídeos no youtube, páginas no stackoverflow e documentações de ferramentas.
