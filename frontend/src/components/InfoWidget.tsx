import { Calendar, CheckCircle, FileQuestion, TrendingUp } from "lucide-react";
import { Card, CardContent, CardHeader, CardTitle } from "@/components/ui/card";
import { cn } from "@/lib/utils";

interface Widget {
  title: string;
  value: string;
  icon: React.ReactNode;
}

const InfoWidget = () => {
  const widgets: Widget[] = [
    {
      title: "Next Session",
      value: "Tomorrow, 2 PM",
      icon: <Calendar className="w-5 h-5" />,
    },
    {
      title: "Attendance",
      value: "85% Complete",
      icon: <CheckCircle className="w-5 h-5" />,
    },
    {
      title: "Upcoming Quiz",
      value: "3 Days",
      icon: <FileQuestion className="w-5 h-5" />,
    },
    {
      title: "Progress",
      value: "Level 4",
      icon: <TrendingUp className="w-5 h-5" />,
    },
  ];

  return (
    <div className="space-y-4 p-4">
      <h3 className="text-lg font-semibold text-[hsl(var(--foreground))]">Quick Access</h3>
      <div className="space-y-3">
        {widgets.map((widget, index) => (
          <Card
            key={index}
            className={cn(
              "border-2 border-[hsl(var(--primary))] bg-[hsl(var(--card))]",
              "hover:gold-glow transition-smooth cursor-pointer"
            )}
          >
            <CardHeader className="pb-3">
              <CardTitle className="text-sm font-medium text-[hsl(var(--muted-foreground))] flex items-center gap-2">
                <span className="text-[hsl(var(--primary))]">{widget.icon}</span>
                {widget.title}
              </CardTitle>
            </CardHeader>
            <CardContent>
              <p className="text-lg font-bold text-[hsl(var(--foreground))]">{widget.value}</p>
            </CardContent>
          </Card>
        ))}
      </div>
    </div>
  );
};

export default InfoWidget;
