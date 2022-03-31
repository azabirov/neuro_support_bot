import json
import urllib.request
import os
from dotenv import load_dotenv
import requests
import argparse


def create_intent(project_id, display_name, training_phrases_parts, message_texts):
    from google.cloud import dialogflow

    intents_client = dialogflow.IntentsClient()

    parent = dialogflow.AgentsClient.agent_path(project_id)
    training_phrases = []
    for training_phrases_part in training_phrases_parts:
        part = dialogflow.Intent.TrainingPhrase.Part(text=training_phrases_part)
        # Here we create a new training phrase for each provided part.
        training_phrase = dialogflow.Intent.TrainingPhrase(parts=[part])
        training_phrases.append(training_phrase)

    text = dialogflow.Intent.Message.Text(text=message_texts)
    message = dialogflow.Intent.Message(text=text)

    intent = dialogflow.Intent(
        display_name=display_name, training_phrases=training_phrases, messages=[message]
    )

    response = intents_client.create_intent(
        request={"parent": parent, "intent": intent}
    )

    print("Intent created: {}".format(response))


def main():
    load_dotenv()

    parser = argparse.ArgumentParser(
        description='Data that you sent via a JSON file link will be put into DialogFlow project.'
    )
    parser.add_argument('link', help='Link to a JSON file')
    args = parser.parse_args()

    # Передается ссылка на JSON файл с информацией для DialogFlow
    # Пример файла
    # https://dvmn.org/media/filer_public/a7/db/a7db66c0-1259-4dac-9726-2d1fa9c44f20/questions.json

    response = requests.get(args.link)
    response.raise_for_status()
    questions = response.json()

    for question in questions:
        create_intent(
            os.environ.get("PROJECT_ID"),
            question,
            questions[question]["questions"],
            [questions[question]["answer"]],
        )


if __name__ == "__main__":
    main()