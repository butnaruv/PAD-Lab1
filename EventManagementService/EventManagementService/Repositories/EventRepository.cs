using EventManagementService.Data;
using EventManagementService.Entities;
using Microsoft.EntityFrameworkCore;

namespace EventManagementService.Repositories
{
    public class EventRepository : IEventRepository
    {
        private readonly DbContextClass _dbContext;

        public EventRepository(DbContextClass dbContext)
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

        public async Task<Event> CreateEventAsync(Event dbEvent)
        {
            Console.WriteLine("entered the create event async from manager service");
            var result = _dbContext.Event.Add(dbEvent);
            try
            {
                await _dbContext.SaveChangesAsync();
            }
            catch (Exception ex)
            {

            }
            return result.Entity;
        }

        public async Task<Event> UpdateEventAsync(Event dbEvent)
        {
            var result = _dbContext.Event.Update(dbEvent);
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
