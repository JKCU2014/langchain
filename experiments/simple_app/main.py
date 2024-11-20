from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate


def main():
    model = ChatOpenAI(model="gpt-4o-mini")
    system_template = "Translate the following from English into {language}"
    prompt_template = ChatPromptTemplate.from_messages(
        [("system", system_template), ("user", "{text}")]
    )
    chain = prompt_template | model
    response = chain.invoke({"language": "Italian", "text": "hi!"})
    print(response.content)
    return 0

if __name__ == "__main__":
    main()
