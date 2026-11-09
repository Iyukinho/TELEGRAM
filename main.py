from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes, MessageHandler, filters

async def start(update:Update, context:ContextTypes.DEFAULT_TYPE):
    user = update.message.from_user
    nome_user = user.username
    await update.message.reply_text(f"Olá, como posso ajudar?\nComandos disponíveis:\n/Start - Inicializa o bot\n/Secretaria\n/Financeiro\n/Calendario - Calendário Acadêmico do semestre\n/Ouvidoria - Canal direto de comunicação")

async def secretaria(update:Update, context:ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(f"Sobre assuntos de Secretaria, como posso te ajudar?\n/Matricula\n/RA - Registro acadêmico\n/Cadastro - Dados cadastrais")

async def matricula(update:Update, context:ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(f"Sobre matrículas ou rematrículas, como posso te ajudar?\n/Rematricula\n/Status - Status da matrícula\n/DP - Reprovação (DP)\n/Grade - Ajuste de grade")

async def rematricula(update:Update, context:ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(f"Que bom que você quer continuar conosco, para continuar sua rematrícula basta pagar o boleto de Janeiro de 2027, caso não queira, basta apenas não seguir com o pagamento")

async def status(update:Update, context:ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(f"Sua matrícula está com o status: ATIVO")

async def dp(update:Update, context:ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(f"Com base no seu boletim, não há nenhuma DP disponível a ser feita")

async def grade(update:Update, context:ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(f"Gostaria de ajustar qual grade?\n/Programacao - Lógica de Programação\n/FrontEnd - Desenvolvimento FrontEnd\n/Empreendedorismo")

async def programacao(update:Update, context:ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(f"Seu momento de falar é agora, me diga tudo o que precisa ser alterado na sua grade")

async def frontend(update:Update, context:ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(f"Seu momento de falar é agora, me diga tudo o que precisa ser alterado na sua grade")

async def empreendedorismo(update:Update, context:ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(f"Seu momento de falar é agora, me diga tudo o que precisa ser alterado na sua grade")
                                                                        
async def ra(update:Update, context:ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(f"Seu RA é: 45226983")

async def cadastro(update:Update, context:ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(f"Seu momento de falar é agora, me diga tudo o que precisa ser alterado no seu cadastro")

async def financeiro(update:Update, context:ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(f"Para poder te ajudar melhor, sobre o que gostaria de falar sobre a parte financeira?\n/Pagamentos - Boletos em aberto ou realizados\n/IR - Declaração de imposto de renda")

async def pagamentos(update:Update, context:ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(f"Gostaria de falar sobre o que?\n/Boletos - Boletos em aberto\n/Realizados - Pagamentos realizados")

async def boletos(update:Update, context:ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(f"Não há boletos em aberto. Caso precise fazer outras solicitações, por favor, digite /Start novamente.")

async def realizados(update:Update, context:ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(f"Gostaria de falar sobre qual desses meses?\n/Julho - 07/2026\n/Agosto - 08/2026\n/Setembro - 09/2026\n/Outubro - 10/2026\n/Novembro - 11/2026")

async def julho(update:Update, context:ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(f"Segue abaixo a sua solicitação")

async def agosto(update:Update, context:ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(f"Segue abaixo a sua solicitação")

async def setembro(update:Update, context:ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(f"Segue abaixo a sua solicitação")

async def outubro(update:Update, context:ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(f"Segue abaixo a sua solicitação")

async def novembro(update:Update, context:ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(f"Segue abaixo a sua solicitação")

async def IR(update:Update, context:ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(f"No meu sistema consta que você se matriculou em 2026, no momento o IR não está disponível. Caso precise fazer outras solicitações, por favor, digite /Start novamente.")

async def calendario(update:Update, context:ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(f"Segue abaixo o seu calendário acadêmico do período de Julho de 2026 à Dezembro de 2026:")

async def ouvidoria(update:Update, context:ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(f"A Ouvidoria é o espaço para você me contar tudo, apresentar sugestões, solicitações e até reclamar um pouquinho. Me conta, sobre o que você quer falar? \n/Sugestoes \n/Queixas \n/Elogios")

async def queixas(update:Update, context:ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(f"Seu momento de falar é agora, me diga tudo detalhado para que possamos te atender")

async def receber_mensagem(update: Update, context: ContextTypes.DEFAULT_TYPE):
    nome = update.message.text

    await update.message.reply_text(f"Abertura de ticket realizada, temos um prazo de até 2 dias para atender sua solicitação. Caso precise fazer outras solicitações, por favor, digite /Start novamente.")

async def sugestoes(update:Update, context:ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(f"Seu momento de falar é agora, me diga tudo detalhado para que possamos te atender")

async def elogios(update:Update, context:ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(f"Seu momento de falar é agora, me diga tudo detalhado para que possamos te atender")

app = ApplicationBuilder().token("8937767536:AAFOMbQk3rwmCE48cwTieFTguYIJTEWoGJI").build()
print("testando")
app.add_handler(CommandHandler("secretaria", secretaria))
app.add_handler(CommandHandler("matricula", matricula))
app.add_handler(CommandHandler("rematricula", rematricula))
app.add_handler(CommandHandler("status", status))
app.add_handler(CommandHandler("dp", dp))
app.add_handler(CommandHandler("grade", grade))
app.add_handler(CommandHandler("programacao", programacao))
app.add_handler(CommandHandler("frontend", frontend))
app.add_handler(CommandHandler("empreendedorismo", empreendedorismo))
app.add_handler(CommandHandler("ra", ra))
app.add_handler(CommandHandler("cadastro", cadastro))
app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("financeiro", financeiro))
app.add_handler(CommandHandler("pagamentos", pagamentos))
app.add_handler(CommandHandler("boletos", boletos))
app.add_handler(CommandHandler("realizados", realizados))
app.add_handler(CommandHandler("julho", julho))
app.add_handler(CommandHandler("agosto", agosto))
app.add_handler(CommandHandler("setembro", setembro))
app.add_handler(CommandHandler("outubro", outubro))
app.add_handler(CommandHandler("novembro", novembro))
app.add_handler(CommandHandler("IR", IR))
app.add_handler(CommandHandler("calendario", calendario))
app.add_handler(CommandHandler("ouvidoria", ouvidoria))
app.add_handler(CommandHandler("queixas", queixas))
app.add_handler(CommandHandler("sugestoes", sugestoes))
app.add_handler(CommandHandler("elogios", elogios))
# Recebe mensagens de texto que não sejam comandos
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, receber_mensagem))
app.run_polling()