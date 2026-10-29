# Who should own the AI interface?

A natural-language interface is most useful when there is a gap between what a person wants and what a system asks them to specify. That gap, rather than the mere presence of an LLM, is what interests me.

Consider buying a train ticket. Sometimes the task is already precise: a known route, a departure time, and an available seat. A well-designed form can handle it directly. At other times, the actual request is closer to “get me there comfortably, with enough time for a transfer, at a reasonable price.” The service needs a structured booking, while the person begins with a bundle of preferences and constraints.

## The interface belongs close to the person

My working intuition is that the layer translating intent into action should often be a personal agent. It can carry context across services: what the user means by a comfortable journey, which trade-offs matter, and which decisions still need an explicit choice.

A service provider has a different kind of knowledge. It knows inventory, prices, operating rules, and the transactions it can support. These responsibilities are complementary. A personal agent should understand the person; a service interface should describe the service accurately and expose dependable operations.

This suggests a simple division of labor: the person expresses an intention, their agent resolves the context, and the service interface supplies authoritative options and actions. The backend remains responsible for what can actually be booked or changed.

## A chatbot on every website is not the whole answer

Adding conversation to an existing interface can help. But making the user explain themselves from scratch to a different assistant at every service loses much of the value of a persistent agent.

The more interesting design problem is interoperability. What must a service expose for an agent to compare options reliably? How should it represent constraints and uncertainty? When should the interaction return to the person? A successful system needs these boundaries to be legible, both to the agent and to the user.

I am especially interested in how this changes human–AI interaction. The interface might become less tied to a particular website and more tied to an ongoing relationship with a user. Evaluating it then means examining whether it preserves intent across an entire task, rather than judging isolated answers.

## An open design question

“Who owns the interface?” is ultimately a question about where understanding lives. My preference is to put personal context near the user, and operational truth near the service. The difficult work is making the connection between them dependable.
