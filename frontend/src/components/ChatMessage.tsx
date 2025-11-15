import { cn } from "@/lib/utils";
import { Bot, User } from "lucide-react";

interface ChatMessageProps {
  role: "user" | "assistant";
  content: string;
}

const ChatMessage = ({ role, content }: ChatMessageProps) => {
  const isUser = role === "user";

  return (
    <div
      className={cn(
        "flex gap-4 px-6 py-4 animate-in fade-in slide-in-from-bottom-4 duration-500",
        isUser ? "justify-end" : "justify-start"
      )}
    >
      {!isUser && (
        <div className="w-8 h-8 rounded-full bg-[hsl(var(--primary))] flex items-center justify-center flex-shrink-0 gold-glow">
          <Bot className="w-5 h-5 text-[hsl(var(--primary-foreground))]" />
        </div>
      )}
      
      <div
        className={cn(
          "max-w-[70%] rounded-2xl px-4 py-3 transition-smooth",
          isUser
            ? "bg-[hsl(var(--user-message-bg))] text-[hsl(var(--user-message-text))]"
            : "bg-[hsl(var(--ai-message-bg))] text-[hsl(var(--ai-message-text))] border border-[hsl(var(--border))] gold-glow"
        )}
      >
        <p className="text-sm leading-relaxed whitespace-pre-wrap">{content}</p>
      </div>

      {isUser && (
        <div className="w-8 h-8 rounded-full bg-[hsl(var(--secondary))] flex items-center justify-center flex-shrink-0">
          <User className="w-5 h-5 text-[hsl(var(--secondary-foreground))]" />
        </div>
      )}
    </div>
  );
};

export default ChatMessage;
