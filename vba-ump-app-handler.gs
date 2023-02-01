function splitAnswerIntoParts(answer) {
  let parts = [];
  try {
    parts = answer.match(/[\s\S]{1,1024}/g) || [];
  } catch (e) {
    parts = answer;
  }
  return parts;
}

function buildItems(question, parts) {
  const items = [];
  for (let i = 0; i < parts.length; i++) {
    if (i === 0) {
      items.push({
        name: question,
        value: parts[i],
        inline: false
      });
    } else {
      items.push({
        name: question.concat(" (cont.)"),
        value: parts[i],
        inline: false
      });
    }
  }
  return items;
}

const POST_URL = ""; // Webhook URL here

function onSubmit(e) {
  const response = e.response.getItemResponses();
  let items = [];

  for (const responseAnswer of response) {
    const question = responseAnswer.getItem().getTitle();
    const answer = responseAnswer.getResponse();
    if (!answer) {
      continue;
    }

    const parts = splitAnswerIntoParts(answer);
    items = [...items, ...buildItems(question, parts)];
  }

  const payload = {
    content: "‌",
    embeds: [
      {
        title: "VBA Ump Form Application",
        color: 33023,
        fields: items,
        footer: {
          text: ""
        },
        timestamp: new Date().toISOString()
      }
    ]
  };

  UrlFetchApp.fetch(POST_URL, {
    method: "post",
    headers: {
      "Content-Type": "application/json"
    },
    payload: JSON.stringify(payload)
  });
}
