# Auditoria e reformulação — 18/10/2026

Repositório: `aldenirfilho/AUDITORIA-E-TRANSPAR-NCIA-DE-IGREJAS-CRISTAS-AO-LONGO-DAS-ERAS-`.
Base examinada: `5201d44`. Direção visual: Turbo TEMI 360X / Turbo X Profânico.

## Achados e tratamento

| Achado | Evidência na base | Tratamento nesta versão |
| --- | --- | --- |
| Home truncada | `index.html` substituía seções por comentário “Full content truncated…” e deixava rodapé vazio | Home reescrita na fonte e nove páginas reconstruídas por `build.py` |
| CSS incompleto | `style.css` terminava com promessa de conteúdo “truncated for brevity” | Componentes completos recuperados do histórico; novo tema em `turbo.css` |
| Filtros sem efeito visual | JavaScript aplicava `.is-hidden`, sem regra correspondente no CSS | Ocultação com `hidden`, busca combinada, contador e estado vazio |
| Hero inválido | `assets/hero-aerospace.jpg` era texto, não um JPEG | Arquivo legado preservado sem uso; nova capa válida e otimizada |
| Atualizações sem referência correspondente | Becciu 2026, Osório setembro/2026, SBC 2025, McCarrick 2023, Bateman estadual/2026 | Fontes específicas acrescentadas às fichas e ao catálogo |
| Catálogo chamado integralmente de primário | Incluía também imprensa e respostas institucionais | Naturezas explicitadas; novas fontes classificadas individualmente |
| Data global sugeria atualização de todos os autos | Rodapé falava em última revisão das pesquisas | Data de edição distinguida da data documental e da consulta |
| Fontes externas sem uso | Fontshare/Google carregados, embora tema usasse Arial | Requisições removidas; famílias locais do sistema |

## Conteúdo entregue

- Oito dossiês novos: Hospital Padre Zé, MEC/pastores, irmandades do Rio, Caldwell, Medina, Davis, Haigler e IOR/Caloia.
- Dezessete referências nos novos dossiês, com datas, origem, contraditório e limites. Ministério Público é fonte da acusação; não substitui acesso integral aos autos.
- Contraponto do STJ sobre validade de contribuição por cheque em processo distinto dos casos de coação.
- Ampliação do método: pacto editorial, correção de informação e proteção contra fraudes de afinidade.
- Dez ilustrações com IA; originais PNG preservados e JPEGs web de até 250 KiB. Prompts e hashes publicados na documentação.
- Trinta fichas do panorama e dez fichas da página Fé e dinheiro preservadas.

## Validação executada

- `python3 build.py`: nove páginas geradas.
- `python3 scripts/validate.py`: fontes/gerados sincronizados, links e âncoras locais válidos, assets presentes, IDs únicos, oito dossiês, dez imagens com hashes válidos, contagem histórica preservada.
- `node --check app.js`: sintaxe válida.
- `git diff --check`: sem erros de whitespace.
- Navegador integrado: nove páginas em 375 px sem overflow horizontal nem imagens quebradas entre as carregadas. Nove páginas também conferidas em 1365 px sem overflow horizontal. Conferência visual da home em 1365 px e 375 px; coleção com 10/10 imagens carregadas. Nenhum erro ou aviso de console capturado no percurso.
- Novos dossiês: 8/8 inicial; Brasil 3/8; Brasil + “Padre” 1/8; termo inexistente 0/8 com aviso visível.
- Panorama: Brasil 6/30. Fé e dinheiro: condenação criminal 5/10.
- Menu móvel abre; Escape fecha e devolve foco ao botão.
- Calculadora preservada: R$ 10 milhões no modo saúde ≈364–571; restauração ≈526 hectares, com premissas visíveis.

## Limites e revisão humana

- Não houve auditoria contábil de transações nem acesso integral a todos os autos. O acervo histórico não foi integralmente reapurado caso a caso.
- Consulta às fontes não comprova inexistência de decisão posterior. Trânsito em julgado só é afirmado quando explicitado na fonte.
- Algumas manifestações defensivas vêm da imprensa ou da própria instituição; as lacunas estão identificadas.
- Acessibilidade foi examinada por estrutura, teclado, busca e responsividade; não houve homologação com leitor de tela ou todos os navegadores/dispositivos físicos.
- Esta entrega deve permanecer em PR rascunho até revisão editorial humana e comparação antes/depois. O merge e a publicação no GitHub Pages dependem dessa revisão.

## Segurança, privacidade e reversão

Site estático, sem login, formulários de denúncia, rastreamento, telemetria, armazenamento pessoal ou APIs externas em execução. Links de fontes só são abertos por ação do leitor. As imagens são metáforas fictícias, sem atribuir crimes a pessoas retratadas. Originais e histórico Git preservados. Para reverter, reverta o commit desta reformulação; a base é `5201d44`.
