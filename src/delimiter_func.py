def split_nodes_delimiter(old_nodes: list[TextNode], delimiter: str, text_type: TextType) -> list[TextNode]:
    new_node = []

    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_node.append(node)
            continue
        
        parts_of_node = node.text.split(delimiter)

        if len(parts_of_node) % 2 == 0:
                raise Exception(f"Unmatched delimiter. {delimiter}")
        for i in range(len(parts_of_node)):
            if parts_of_node[i] == "": 
                continue
            if i % 2 == 0:
                new_node.append(TextNode(parts_of_node[i], TextType.TEXT))
            else:
                new_node.append(TextNode(parts_of_node[i], text_type))
    return new_node