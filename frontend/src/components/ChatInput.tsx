import { useState } from "react";
import { Send } from "lucide-react";
import { Button } from "@/components/ui/button";
import { Textarea } from "@/components/ui/textarea";
import { cn } from "@/lib/utils";

interface ChatInputProps {
  onSend: (message: string) => void;
  disabled?: boolean;
}

const ChatInput = ({ onSend, disabled }: ChatInputProps) => {
  const [message, setMessage] = useState("");

  const handleSubmit = (e: React.FormEvent) => {
    e.preventDefault();
    if (message.trim() && !disabled) {
      onSend(message);
      setMessage("");
    }
  };

  const handleKeyDown = (e: React.KeyboardEvent<HTMLTextAreaElement>) => {
    if (e.key === "Enter" && !e.shiftKey) {
      e.preventDefault();
      handleSubmit(e);
    }
  };

  return (
    <form onSubmit={handleSubmit} className="border-t border-[hsl(var(--border))] p-4 bg-[hsl(var(--card))]">
      <div className="flex gap-3 items-end max-w-4xl mx-auto">
        <Textarea
          value={message}
          onChange={(e) => setMessage(e.target.value)}
          onKeyDown={handleKeyDown}
          placeholder="Type your PRP question here..."
          className={cn(
            "min-h-[60px] max-h-[200px] resize-none",
            "bg-[hsl(var(--input))] border-[hsl(var(--border))]",
            "text-[hsl(var(--foreground))] placeholder:text-[hsl(var(--muted-foreground))]",
            "focus:ring-2 focus:ring-[hsl(var(--ring))] transition-smooth"
          )}
          disabled={disabled}
        />
        <Button
          type="submit"
          disabled={!message.trim() || disabled}
          className={cn(
            "rounded-full w-12 h-12 p-0 flex items-center justify-center",
            "bg-[hsl(var(--primary))] hover:bg-[hsl(var(--primary))] hover:scale-110",
            "gold-glow transition-smooth",
            "disabled:opacity-50 disabled:cursor-not-allowed disabled:hover:scale-100"
          )}
        >
          <Send className="w-5 h-5 text-[hsl(var(--primary-foreground))]" />
        </Button>
      </div>
    </form>
  );
};

export default ChatInput;
