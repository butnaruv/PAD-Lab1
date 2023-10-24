using TaskManagementService.Entites;
using System;
using TaskManagementService.Protos;

namespace TaskManagementService.Repositories
{
    public interface ITaskRepository
    {
        public Task<List<TaskModel>> GetTaskListByEventIdAsync(GetByEvent eventId);
        public Task<TaskModel> GetTaskByIdAsync(int taskId);
        public Task<TaskModel> CreateTaskAsync(TaskModel task);
        public Task<TaskModel> UpdateTaskAsync(TaskModel task);
        public Task<bool> DeleteTaskAsync(int taskId);
    }
}
