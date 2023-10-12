using TaskManagementService.Entites;
using System;

namespace TaskManagementService.Repositories
{
    public interface ITaskManagerService
    {
        public Task<List<TaskModel>> GetTaskListByEventIdAsync(int eventId);
        public Task<TaskModel> GetTaskByIdAsync(int taskId);
        public Task<TaskModel> CreateTaskAsync(TaskModel task);
        public Task<TaskModel> UpdateTaskAsync(TaskModel task);
        public Task<bool> DeleteTaskAsync(int taskId);
    }
}
