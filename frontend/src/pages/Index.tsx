import { useState, useRef, useEffect } from "react";
import { Menu, X } from "lucide-react";
import Sidebar from "@/components/Sidebar";
import ChatMessage from "@/components/ChatMessage";
import ChatInput from "@/components/ChatInput";
import InfoWidget from "@/components/InfoWidget";
import { Button } from "@/components/ui/button";
import { cn } from "@/lib/utils";

interface Message {
  role: "user" | "assistant";
  content: string;
}

const Index = () => {
  const [messages, setMessages] = useState<Message[]>([]);
  const [isSidebarCollapsed, setIsSidebarCollapsed] = useState(false);
  const [showWidgets, setShowWidgets] = useState(false);
  const messagesEndRef = useRef<HTMLDivElement>(null);

  const scrollToBottom = () => {
    messagesEndRef.current?.scrollIntoView({ behavior: "smooth" });
  };

  useEffect(() => {
    scrollToBottom();
  }, [messages]);

  const handleSendMessage = (content: string) => {
    // Add user message
    setMessages((prev) => [...prev, { role: "user", content }]);

    // Simulate AI response
    setTimeout(() => {
      setMessages((prev) => [
        ...prev,
        {
          role: "assistant",
          content: "Hello! I'm the PRP AI Agent. I'm here to help you with all your Professional Readiness Program questions. You can ask me about badges, events, attendance, quizzes, and track your progress. How can I assist you today?",
        },
      ]);
    }, 1000);
  };

  return (
    <div className="flex h-screen w-full overflow-hidden">
      {/* Sidebar */}
      <Sidebar isCollapsed={isSidebarCollapsed} />

      {/* Main Chat Area */}
      <div className="flex-1 flex flex-col">
        {/* Header */}
        <header className="border-b border-[hsl(var(--border))] bg-[hsl(var(--card))] px-6 py-4">
          <div className="flex items-center justify-between">
            <div className="flex items-center gap-3">
              <Button
                variant="ghost"
                size="icon"
                onClick={() => setIsSidebarCollapsed(!isSidebarCollapsed)}
                className="hover:bg-[hsl(var(--accent))] transition-smooth"
              >
                {isSidebarCollapsed ? <Menu className="w-5 h-5" /> : <X className="w-5 h-5" />}
              </Button>
              <div>
                <h1 className="text-xl font-bold text-[hsl(var(--foreground))] flex items-center gap-2">
                  Mentra - PRP AI Agent 🤖
                </h1>
                <p className="text-sm text-[hsl(var(--muted-foreground))]">
                  Your AI Haven for Your Career Elevation
                </p>
              </div>
            </div>
            <Button
              variant="ghost"
              size="sm"
              onClick={() => setShowWidgets(!showWidgets)}
              className="hover:bg-[hsl(var(--accent))] transition-smooth"
            >
              {showWidgets ? "Hide" : "Show"} Widgets
            </Button>
          </div>
          <p className="text-xs text-[hsl(var(--muted-foreground))] mt-2 italic">
            "I’m here to make your PRP journey easier, one question at a time."
          </p>
        </header>

        {/* Chat Container */}
        <div className="flex-1 flex overflow-hidden">
          {/* Messages Area */}
          <div className="flex-1 flex flex-col">
            <div className="flex-1 overflow-y-auto">
              {messages.length === 0 ? (
                <div className="h-full flex items-center justify-center p-6">
                  <div className="text-center max-w-2xl">
                    <div className="w-20 h-20 rounded-full bg-[hsl(var(--primary))] mx-auto mb-6 flex items-center justify-center gold-glow animate-pulse">
                      <span className="text-4xl">🤖</span>
                    </div>
                    <h2 className="text-3xl font-bold text-[hsl(var(--foreground))] mb-4 text-glow">
                      Welcome to Mentra – PRP AI Agent
                    </h2>
                    <p className="text-[hsl(var(--muted-foreground))] mb-8 text-lg">
                      Ready to track your PRP progress today? I can help you with:
                    </p>
                    <div className="grid grid-cols-2 gap-4 text-left">
                      {[
                        "📖 Learn About PRP",
                        "📊 Check My Attendance",
                        "📅 What’s Coming Up?",
                        "📝 My Quizzes & Results",
                        "🏆 My Badge Progress",
                        "📈 My PRP Overview",
                        "🤝 Mentor Me, Mentra",
                      ].map((item, index) => (
                        <div
                          key={index}
                          className={cn(
                            "p-4 rounded-lg bg-[hsl(var(--card))] border border-[hsl(var(--border))]",
                            "hover:border-[hsl(var(--primary))] hover:gold-glow transition-smooth cursor-default"
                          )}
                        >
                          <p className="text-sm text-[hsl(var(--foreground))]">{item}</p>
                        </div>
                      ))}
                    </div>
                    <Button
                      onClick={() => handleSendMessage("Hello!")}
                      className={cn(
                        "mt-8 px-8 py-6 text-lg font-semibold rounded-full",
                        "bg-[hsl(var(--primary))] hover:bg-[hsl(var(--primary))] hover:scale-105",
                        "gold-glow transition-smooth"
                      )}
                    >
                      Start Chatting
                    </Button>
                  </div>
                </div>
              ) : (
                <div className="py-4">
                  {messages.map((message, index) => (
                    <ChatMessage key={index} role={message.role} content={message.content} />
                  ))}
                  <div ref={messagesEndRef} />
                </div>
              )}
            </div>

            {/* Input Area */}
            <ChatInput onSend={handleSendMessage} />
          </div>

          {/* Right Widget Panel */}
          {showWidgets && (
            <div className="w-80 border-l border-[hsl(var(--border))] bg-[hsl(var(--card))] overflow-y-auto">
              <InfoWidget />
            </div>
          )}
        </div>
      </div>
    </div>
  );
};

export default Index;
