using Microsoft.EntityFrameworkCore;
using System;
using TaskManagementService.Data;
using TaskManagementService.Entites;

namespace TaskManagementService.Repositories
{
    public class TaskManagerService : ITaskManagerService
    {
        private readonly DbContextClass _dbContext;
        public TaskManagerService(DbContextClass dbContext)
        {
            _dbContext = dbContext;
        }
        public async Task<TaskModel> CreateTaskAsync(TaskModel task)
        {
            var result = _dbContext.Task.Add(task);
            await _dbContext.SaveChangesAsync();
            return result.Entity;
        }

        public async Task<bool> DeleteTaskAsync(int taskId)
        {
            throw new NotImplementedException();
        }

        public async Task<TaskModel> GetTaskByIdAsync(int taskId)
        {
            throw new NotImplementedException();
        }

        public async Task<List<TaskModel>> GetTaskListByEventIdAsync(int eventId)
        {
            return await _dbContext.Task
        .Where(task => task.EventId == eventId)
        .ToListAsync();
        }

        public Task<TaskModel> UpdateTaskAsync(TaskModel task)
        {
            throw new NotImplementedException();
        }
    }
}
