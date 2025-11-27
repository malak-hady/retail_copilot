import json, click
from agent.graph_hybrid import HybridGraph

@click.command()
@click.option('--batch', required=True, help="JSONL file with questions")
@click.option('--out', required=True, help="Output JSONL file")
def main(batch, out):
    graph = HybridGraph()
    outputs = []

    with open(batch, 'r', encoding='utf-8-sig') as f:

        for line in f:
            q = json.loads(line)
            result = graph.run(q['question'], q['id'], q['format_hint'])
            outputs.append({
                "id": q['id'],
                "final_answer": result["final_answer"],
                "sql": result["sql"],
                "confidence": result["confidence"],
                "explanation": result["explanation"],
                "citations": result["citations"]
            })

    
    with open(out, 'w', encoding='utf-8') as f:
        for r in outputs:
            f.write(json.dumps(r, ensure_ascii=False)+'\n')

if __name__ == '__main__':
    main()
