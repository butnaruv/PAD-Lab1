using Microsoft.EntityFrameworkCore;
using System;
using TaskManagementService.Data;
using TaskManagementService.Entites;
using TaskManagementService.Protos;

namespace TaskManagementService.Repositories
{
    public class TaskRepository : ITaskRepository
    {
        private readonly DbContextClass _dbContext;
        public TaskRepository(DbContextClass dbContext)
        {
            _dbContext = dbContext;
        }
        public async Task<TaskModel> CreateTaskAsync(TaskModel task)
        {
            try
            {
                var result = _dbContext.Task.Add(task);
                await _dbContext.SaveChangesAsync();
                return result.Entity;
            }
            catch (Exception ex)
            {

            }
            return null;
        }

        public async Task<bool> DeleteTaskAsync(int taskId)
        {
            var filteredData = _dbContext.Task.Where(x => x.Id == taskId).FirstOrDefault();
            var result = _dbContext.Remove(filteredData);
            await _dbContext.SaveChangesAsync();
            return result != null ? true : false;
        }

        public async Task<TaskModel> GetTaskByIdAsync(int taskId)
        {
            return await _dbContext.Task.Where(x => x.Id == taskId).FirstOrDefaultAsync();

        }

        public async Task<List<TaskModel>> GetTaskListByEventIdAsync(GetByEvent eventId)
        {
            return await _dbContext.Task
        .Where(task => task.EventId == eventId.EventId)
        .ToListAsync();
        }

        public async Task<TaskModel> UpdateTaskAsync(TaskModel task)
        {
            var result = _dbContext.Task.Update(task);
            await _dbContext.SaveChangesAsync();
            return result.Entity;
        }
    }
}
