namespace TaskManagementService.Entites
{
    public class TaskModel
    {
        public int TaskId { get; set; }
        public int EventId { get; set; }
        public string Name { get; set; }
        public string Description { get; set; }
        public string Deadline { get; set; }
        public string Status { get; set; }
    }
}
