using EventManagementService.Data;
using EventManagementService.Entities;
using Microsoft.EntityFrameworkCore;
using System;

namespace EventManagementService.Repositories
{
    public class EventManagerService: IEventManagerService
    {
        private readonly DbContextClass _dbContext;

        public EventManagerService(DbContextClass dbContext)
        {
            _dbContext = dbContext;
        }

        public async Task<List<Event>> GetEventListAsync()
        {
            return await _dbContext.Event.ToListAsync();
        }

        public async Task<Event> GetEventByIdAsync(int Id)
        {
            return await _dbContext.Event.Where(x => x.Id == Id).FirstOrDefaultAsync();
        }

        public async Task<Event> CreateEventAsync(Event offer)
        {
            var result = _dbContext.Event.Add(offer);
            await _dbContext.SaveChangesAsync();
            return result.Entity;
        }

        public async Task<Event> UpdateEventAsync(Event offer)
        {
            var result = _dbContext.Event.Update(offer);
            await _dbContext.SaveChangesAsync();
            return result.Entity;
        }
        public async Task<bool> DeleteEventAsync(int Id)
        {
            var filteredData = _dbContext.Event.Where(x => x.Id == Id).FirstOrDefault();
            var result = _dbContext.Remove(filteredData);
            await _dbContext.SaveChangesAsync();
            return result != null ? true : false;
        }
    }
}
