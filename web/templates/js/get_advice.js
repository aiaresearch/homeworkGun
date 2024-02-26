const dataContainer = document.getElementById('data-container');
let accumulatedData = '';

const fetchDataStream = async () => {
    const response = await fetch('http://localhost:5000/get-data');
    const reader = response.body.getReader();
    return new ReadableStream({
        async start(controller) {
            while (true) {
                const { done, value } = await reader.read();
                if (done) {
                    break;
                }
                const chunk = new TextDecoder("utf-8").decode(value);
                accumulatedData += chunk;
                processChunk();
                controller.enqueue(value);
            }
            controller.close();
            reader.releaseLock();
        }
    });
};

const processChunk = () => {
    const messages = accumulatedData.split('\n').filter(Boolean);
    messages.forEach(message => {
        try {
            const dataObj = JSON.parse(message);
            const contentObj = JSON.parse(dataObj.content);
            if(contentObj.someKey) {
                contentObj.someKey.forEach(char => displayData(char));
            }
        } catch (error) {
            // wait for more data
            console.error('Error processing chunk', error);
        }
    });
    accumulatedData = '';
};

const displayData = (char) => {
    if (char === '\n') { // 检查是否需要换行
        const breakElement = document.createElement('br');
        dataContainer.appendChild(breakElement);
    } else {
        const spanElement = document.createElement('span');
        spanElement.textContent = char;
        dataContainer.appendChild(spanElement);
    }
};

fetchDataStream();