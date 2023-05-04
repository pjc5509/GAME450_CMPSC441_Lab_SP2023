#salesken/text_generate on hugging face
#https://huggingface.co/salesken/text_generate?text=Bandit+remarks+as+he+runs+away%2C+%22


class Text_Gen:
    from transformers import AutoTokenizer, AutoModelWithLMHead 
    import torch

    device =""

    if torch.cuda.is_available():
            device = torch.device("cuda")
    else :
        device = "cpu"

    tokenizer = AutoTokenizer.from_pretrained("salesken/text_generate")
    model = AutoModelWithLMHead.from_pretrained("salesken/text_generate").to(device)
    
    #Function to create a diolog
    def NGL(self, input_query):      
    
        #input_query="tough challenges make you stronger.  "
        input_ids = self.tokenizer.encode(input_query.lower(), return_tensors='pt').to(self.device)

        sample_outputs = self.model.generate(input_ids,
                                    do_sample=True,
                                    num_beams=1, 
                                    max_length=25,
                                    temperature=0.99,
                                    top_k = 10,
                                    num_return_sequences=1)

        for i in range(len(sample_outputs)):
            print(self.tokenizer.decode(sample_outputs[i], skip_special_tokens=True))

    #this function generate the prompt based on the weapon and a hit 0 is miss
    def responce(self, weapon, miss):
        prompt = ""

        if weapon == 0 and miss == 0:
            prompt = "The sword slashed the bandit. The bandit yelled "
        elif weapon == 1 and miss == 0:
            prompt = "The arrow punctured the bandit. The bandit said in pain "
        elif weapon == 2 and miss == 0:
            prompt = "The fire burned the bandit. The bandit sceamed "
        elif weapon == 0 and miss == 1:
            prompt = "The bandit dodged the sword slash. The bandit yelled "
        elif weapon == 1 and miss == 1:
            prompt = "The bandit caught the arrow. The bandit joked "
        elif weapon == 2 and miss == 1:
            prompt = "The banit ignored the fire. The bandit taunted "
        else:
            prompt = "Something wiered happen in the battle"

        self.NGL( prompt)

